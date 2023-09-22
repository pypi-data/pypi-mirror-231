import torch
import copy
from ..utils.layer import get_cnn_layer
from ..utils.hooks import attach_hooks_to_layer


class CNNRaw():
    def __init__(
        self,
        cnn: torch.nn.Module,
        device: str,
    ):
        self.cnn = copy.deepcopy(cnn).to(device)
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

    def get_layer_kernels(
        self,
        layer_name: str,
        aggregate=False,
    ):
        """
        Retrieves representation of kernels of a specific cnn layer

        Args:
            layer_name (str): Name of the layer

        Returns:
            kernels (torch.tensor): Kernel representations | Shape: (N, C, K)

        Note:
            N: Number of kernels in layer
            C: Number of layer InChannels
            K: Kernel size
        """
        layer = get_cnn_layer(self.cnn, layer_name)
        kernel_weights = layer.weight.data
        return kernel_weights.abs().mean(dim=1) if aggregate else kernel_weights

    def get_specific_kernel(
            self,
            layer_name: str,
            idx_kernel: int,
            aggregate=False,
    ):
        """
        Retrieves representation of a specific kernel

        Args:
            layer_name (str): Name of the layer
            idx_kernel (int): Index of kernel

        Returns:
            kernel (torch.tensor): Kernel representation | Shape: (C, K)

        Note:
            C: Number of layer InChannels
            K: Kernel size
        """
        kernel_weight = self.get_layer_kernels(layer_name)[idx_kernel]
        return kernel_weight.abs().mean(dim=0) if aggregate else kernel_weight

    def get_layer_feature_maps(
        self,
        layer_name: str,
        input_ts: torch.tensor,
    ):
        """
        Retrieves representations of all feature maps in a specific layer

        Args:
            layer_name (str): Name of the layer
            input_ts (torch.tensor): 3D input tensor in the shape (1, C, T)

        Returns:
            feature_maps (torch.tensor): Feature Maps | Shape: (1, N, T)

        Note:
            N: Number of kernels in layer
            T: Length of time series
        """
        # get a tensor copy on device
        input_ts = input_ts.to(self.device)
        # add hook to layer
        self.__setup_layer_hook(layer_name)

        feature_maps = self.__get_layer_activation(input_ts, layer_name)
        return feature_maps

    def get_specific_feature_map(
        self,
        layer_name: str,
        idx_kernel: int,
        input_ts: torch.tensor,
    ):
        """
        Retrieves representations of a specific feature map in a specific layer

        Args:
            layer_name (str): Name of the layer
            idx_kernel (int): Index of specific kernel for the feature map
            input_ts (torch.tensor): 3D input tensor in the shape (1, C, T)

        Returns:
            feature_maps (torch.tensor): Feature Maps | Shape: (T)

        Note:
            T: Length of time series
        """
        return self.get_layer_feature_maps(layer_name, input_ts).squeeze()[idx_kernel]
