import torch
import matplotlib.pyplot as plt

from ..utils.dtw import SoftDTW


class AMResult():
    def __init__(self, result_tensor, device, original_data=None):
        """ Method to construct an AMResult object

        Args:
            result_tensor (torch.tensor): Result given by AM algorithm | Shape (N, C, T)
            device (str): Device used to perform all the actions in this class
            original_data (torch.tensor): Used to compare the generated signals with actual data | Shape (N, C, T)
        """
        assert len(result_tensor.shape) == 3, "Shape of result_tensor has to be (N, C, T)"
        if original_data:
            assert len(original_data.shape) == 3, "Shape of original data has to be (N, C, T)"

        self.device = device
        self.result_tensor = result_tensor.to(self.device)
        self.original_data = original_data.to(self.device) if original_data is not None else None

        self.num_units = self.result_tensor.shape[0]
        self.num_channels = self.result_tensor.shape[1]
        self.ts_length = self.result_tensor.shape[2]

        self.dtw_loss = None

    def set_original_data(self, original_data):
        """ Used to set original data after constructing the object

        Args:
            original_data (torch.tensor): Used to compare the generated signals with actual data | Shape (N, C, T)
        """
        assert len(original_data.shape) == 3, "Shape of original data has to be (N, C, T)"
        self.original_data = original_data.to(self.device)

    def evaluate(self, method: str):
        """ Performs an evaluation of the given result_tensor with DTW or error functions

        Args:
            method (str): Method to use for evaluation

        Note:
            Possible values for method are currently: 'dtw', 'mse', 'mae'
        """
        assert self.original_data is not None, "You need to set the comparison data (usually the training data) first by using result.set_original_data(...)"

        match method:
            case 'dtw':
                return self.__evaluate_dtw()
            case 'mse':
                return self.__evaluate_mse()
            case 'mae':
                return self.__evaluate_mae()
            case _:
                raise Exception(f"The given evaluation method {method} is currently not implemented.")

    def __evaluate_dtw(self):
        """ Calculates the evaluation metric with Dynamic Time Warping

        Returns:
            mean_loss (torch.tensor): Mean loss value over all AM samples (usually kernels)

        Note:
            This function takes a lot of VRAM.
            If your neural net has a lot of kernels, consider performing this operation on the CPU by providing 'cpu' as device to the class.
        """
        loss_fct = SoftDTW()

        losses = torch.zeros((self.num_units, self.original_data.shape[0]))

        for idx_unit in range(self.num_units):
            losses[idx_unit] = loss_fct(self.result_tensor[idx_unit:idx_unit+1, :, :], self.original_data)

        # save it for plotting purposes
        self.dtw_loss = losses

        # get the minimum loss for each unit and then average over those
        mean_loss = losses.min(dim=1).values.mean()

        return mean_loss

    def __evaluate_mse(self):
        raise Exception("Not implemented")

    def __evaluate_mae(self):
        raise Exception("Not implemented")

    def plot_am_output(self, idx_kernel=0, channel=0):
        # prepare result tensor for plotting
        plot_tensor = self.result_tensor[idx_kernel][channel].cpu().detach()

        plt.figure(figsize=(16, 5))
        plt.plot(plot_tensor, 'b-')
        plt.show()
