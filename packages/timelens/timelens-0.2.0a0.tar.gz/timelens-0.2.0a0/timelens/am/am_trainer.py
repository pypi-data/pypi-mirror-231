import torch
import copy

from ..utils.hooks import attach_hooks_to_layer
from ..utils.layer import get_cnn_layer
from .am_penalty import l2_norm, total_variation, extreme_value_penalty
from .am_result import AMResult


class AMTrainer():
    """ Class to handle all the functionality related to activation maximization for time series

    Attributes:
        cnn (torch.nn.module): Convolutional neural network used for the AM process
        device (str): Device to perform all necessary operations on (PyTorch)

    Methods:

    """

    def __init__(self, cnn, device):
        """ Method to construct an AMTrainer object

        Args:
            cnn (torch.nn.module): Convolutional neural network used for the AM process
            device (str): Device to perform all necessary operations on (PyTorch)

        Returns:
            AMTrainer
        """
        # perform a copy of the neural net to not change anything in the referenced neural net
        self.cnn = copy.deepcopy(cnn).to(device)
        self.cnn.eval()

        self.device = device
        self.act_dict = {}

    def __get_layer_activation(self, input, layer_name):
        """ Forward the input through the layer to get the activation of a specific layer

        Args:
            input (torch.tensor): 3-D input tensor in the shape (1, C, T)
            layer_name (str): Name of the layer

        Returns:
            act (torch.tensor): Layer activation in the form of (InputCh, OutputCh)

        """
        self.cnn(input)
        act = self.act_dict[layer_name]
        return act

    def __setup_layer_hook(self, layer_name):
        """ Sets up the layer hook for the specified layer

        Args:
            layer_name (str): Name of the layer to add the hook to
        """
        attach_hooks_to_layer(self.cnn, self.act_dict, layer_name)

    def __prepare_ts(self, input_ts):
        """ Creates a parameter tensor from input_ts and moves it to device

        Args:
            input_ts (np.ndarray): Input time series in shape (1, C, T)

        Returns:
            output_ts (torch.tensor): Parameter tensor on device
        """
        # move input to same device as cnn
        output_ts = torch.from_numpy(input_ts).float().to(self.device)
        output_ts = torch.nn.Parameter(output_ts)
        return output_ts

    def activation_maximization_layer(
            self,
            input_ts,
            layer_name,
            lr=1e-2,
            gamma=0.999,
            iterations=5000,
            penalties=None,
            th_clip=None,
    ):
        """ Performs activation maximization for a specific input for a whole neural net layer

        Args:
            input_ts (torch.tensor): Starting point for AM | Shape: (1, C, T)
            layer_name (str): Layer to perform AM on (e.g. 'conv_layers.conv0')
            lr (float): Learning rate for stochastic gradient descent
            gamma (float): Adaption value for learning rate with scheduler (each iteration)
            iterations (int): Number of AM iterations
            penalties (dict): Contains the necessary configuration for the penalties | Order is relevant
            th_clip (float): Upper value for the clipping of activation values

        Note: The following is the recommend setup for penalties:
            penalties = [
                {
                    'penalty': 'eap',
                    'weight': 0.1,
                    'th': 0.65,
                },
                {
                    'penalty': 'l2',
                    'weight': 0.1,
                },
                {
                    'penalty': 'tv',
                    'weight': 0.1,
                },
            ]

        Returns:
            output_ts (torch.tensor): Input ts that has been adapted by AM | Shape: (N, C, T)
        """
        layer = get_cnn_layer(self.cnn, layer_name)
        num_kernels = layer.out_channels
        num_channels = input_ts.shape[1]
        num_timesteps = input_ts.shape[2]

        am_arr = torch.zeros(num_kernels, num_channels, num_timesteps)

        for idx_kernel in range(num_kernels):
            res = self.activation_maximization(
                input_ts,
                layer_name,
                idx_kernel,
                lr,
                gamma,
                iterations,
                penalties,
                th_clip
            )
            res = res.result_tensor.squeeze(dim=0)
            am_arr[idx_kernel] = res

        return AMResult(am_arr, self.device)

    def activation_maximization(
            self,
            input_ts,
            layer_name,
            idx_kernel,
            lr=1e-2,
            gamma=0.999,
            iterations=5000,
            penalties=None,
            th_clip=None,
    ):
        """ Performs activation maximization for a specific input

        Args:
            input_ts (np.ndarray): Starting point for AM | Shape: (1, C, T)
            layer_name (str): Layer to perform AM on
            idx_kernel (int): Index of the specific kernel in the CNN layer to maximize activations
            lr (float): Learning rate for stochastic gradient descent
            gamma (float): Adaption value for learning rate with scheduler (each iteration)
            iterations (int): Number of AM iterations
            penalties (dict): Contains the necessary configuration for the penalties | Order is relevant
            th_clip (float): Upper value for the clipping of activation values

        Note: The following is the recommend setup for penalties:
            penalties = [
                {
                    'penalty': 'eap',
                    'weight': 0.1,
                    'th': 0.65,
                },
                {
                    'penalty': 'l2',
                    'weight': 0.1,
                },
                {
                    'penalty': 'tv',
                    'weight': 0.1,
                },
            ]

        Returns:
            output_ts (torch.tensor): Input ts that has been adapted by AM | Shape: (1, C, T)
        """
        output_ts = self.__prepare_ts(input_ts)
        optimizer = torch.optim.SGD([output_ts], lr=lr)
        lr_scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=gamma)

        # add hook to layer
        self.__setup_layer_hook(layer_name)

        for idx in range(iterations):
            self.__am_step(output_ts, layer_name, idx_kernel, optimizer, lr_scheduler, penalties, th_clip)

        return AMResult(output_ts, self.device)

    def __am_step(self, input_ts, layer_name, idx_kernel, optimizer, lr_scheduler, penalties, th_clip):
        """ Performs a single activation maximization step by using gradient ascent

        Args:
            input_ts (torch.tensor): Starting point for AM | Shape: (1, C, T)
            layer_name (str): Layer to perform AM on
            idx_kernel (int): Index of the specific kernel in the CNN layer to maximize activations
            optimizer (torch.optim): Optimizer to use for gradient ascent
            lr_scheduler (torch.optim.lr_scheduler): Learning rate scheduler for the optimizer
            penalties (dict): Contains the necessary configuration for the penalties
            th_clip (float): Upper threshold for the clipping of activation values

        Returns:
            None (pass by reference)
        """
        self.cnn.zero_grad()

        # get activation
        acts = self.__get_layer_activation(input_ts, layer_name)
        # filter activations for specific kernel ( (1, OutCh, X) -> (X) )
        acts = acts.squeeze()[idx_kernel]

        # clip activation values
        if th_clip:
            acts = torch.clamp(acts, min=0, max=th_clip)

        # reduce activations to a single value
        acts_reduced = acts.mean()

        # if penalties exist, apply them in the given order
        if penalties:
            for penalty in penalties:
                match penalty['penalty']:
                    case 'eap':
                        acts_reduced = self.__apply_eap(acts_reduced, input_ts, acts, penalty['weight'], penalty['th'])
                    case 'tv':
                        acts_reduced = self.__apply_tv(acts_reduced, input_ts, acts, penalty['weight'])
                    case 'l2':
                        acts_reduced = self.__apply_l2(acts_reduced, input_ts, acts, penalty['weight'])
                    case _:
                        raise Exception(f'Given penalty {penalty.type} does not exist')

        # negate reduced value to perform gradient ascent
        acts_reduced_neg = acts_reduced * -1
        # perform backward propagation to update the input ts
        acts_reduced_neg.backward()
        optimizer.step()
        lr_scheduler.step()

    def __apply_eap(self, act_val, x, acts, w_eap, th):
        """ Calculate extreme value penalty and apply it to the reduced activation

        Args:
            act_val (float): Reduced activation value
            x (torch.tensor): Timeseries that was used to calculate the activations | Shape: (1, C, T)
            acts (torch.tensor): Activation tensor
            w_eap (float): Weight used to apply the penalty
            th (float): Threshold value used for the extreme value penalty

        Returns:
            act_val (float): Adjusted reduced activation value depending on penalty
        """
        penalty_eap = extreme_value_penalty(acts, th)
        penalty_eap_weighted = w_eap * penalty_eap
        act_val -= penalty_eap_weighted
        return act_val

    def __apply_l2(self, act_val, x, acts, w_l2):
        """ Calculate L2 penalty and apply it to the reduced activation

        Args:
            act_val (float): Reduced activation value
            x (torch.tensor): Timeseries that was used to calculate the activations | Shape: (1, C, T)
            acts (torch.tensor): Activation tensor
            w_l2 (float): Weight used to apply the penalty

        Returns:
            act_val (float): Adjusted reduced activation value depending on penalty
        """
        penalty_l2 = l2_norm(x)
        penalty_l2_norm = penalty_l2 / x.numel()
        penalty_l2_weighted = w_l2 * penalty_l2_norm
        # penalty_l2_weighted  = w_l2  * penalty_l2
        act_val -= penalty_l2_weighted
        return act_val

    def __apply_tv(self, act_val, x, acts, w_tv):
        """ Calculate total variation penalty and apply it to the reduced activation

        Args:
            act_val (float): Reduced activation value
            x (torch.tensor): Timeseries that was used to calculate the activations | Shape: (1, C, T)
            acts (torch.tensor): Activation tensor
            w_tv (float): Weight used to apply the penalty

        Returns:
            act_val (float): Adjusted reduced activation value depending on penalty
        """
        penalty_tv = total_variation(x)
        penalty_tv_norm = penalty_tv / x.numel()
        penalty_tv_weighted = w_tv * penalty_tv_norm
        # penalty_tv_weighted  = w_tv * penalty_tv
        act_val -= penalty_tv_weighted
        return act_val

    def reset(self):
        """ Resets the activation dictionary """
        self.act_dict = {}
