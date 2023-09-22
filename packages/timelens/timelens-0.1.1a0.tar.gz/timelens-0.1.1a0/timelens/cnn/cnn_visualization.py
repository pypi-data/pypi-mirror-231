import torch
import numpy as np
import matplotlib.pyplot as plt
from .cnn_utils import normalize_kernel
from .cnn_raw import CNNRaw


class CNNViz(CNNRaw):
    def __init__(
        self,
        cnn: torch.nn.Module,
        device: str,
    ):
        super().__init__(cnn, device)

    def plot_layer_kernels(
        self,
        layer_name: str,
        ncols=4,
        aggregate_kernels=True,
    ):
        """
        Retrieves representation of kernels of a specific cnn layer

        Args:
            layer_name (str): Name of the layer

        Returns:
            None
        """
        kernels = super().get_layer_kernels(layer_name)
        num_kernels = kernels.size(0)

        fig, axs = plt.subplots(
            nrows=int(np.ceil(num_kernels / ncols)),
            ncols=ncols,
            figsize=(16, num_kernels / 2),
        )

        for idx, ax in enumerate(axs.flatten()):
            if idx >= num_kernels:
                ax.set_visible(False)
                continue

            kernel = kernels[idx]
            kernel = normalize_kernel(kernel, aggregate_kernels)
            ax.imshow(kernel.cpu().detach(), cmap="Blues")
            ax.set_title(f"{layer_name}: {idx}")
        plt.show()

    def plot_specific_kernel(
            self,
            layer_name: str,
            idx_kernel: int,
            aggregate_kernels=True,
    ):
        """
        Retrieves representation of a specific kernel

        Args:
            layer_name (str): Name of the layer
            idx_kernel (int): Index of kernel

        Returns:
            None
        """
        kernel = super().get_specific_kernel(layer_name, idx_kernel)

        kernel = normalize_kernel(kernel, aggregate_kernels)
        plt.imshow(kernel.cpu().detach(), cmap="Blues")
        plt.title(f"{layer_name}: {idx_kernel}")
        plt.show()

    def plot_layer_feature_maps(
        self,
        layer_name: str,
        input_ts: torch.tensor,
        ncols=2,
    ):
        """
        Retrieves representations of all feature maps in a specific layer

        Args:
            layer_name (str): Name of the layer
            input_ts (torch.tensor): 3D input tensor in the shape (1, C, T)

        Returns:
            None
        """
        feature_maps = super().get_layer_feature_maps(layer_name, input_ts).squeeze()
        num_feature_maps = feature_maps.size(0)

        fig, axs = plt.subplots(
            nrows=int(np.ceil(num_feature_maps / ncols)),
            ncols=ncols,
            figsize=(16, num_feature_maps/0.5),
        )

        for idx, ax in enumerate(axs.flatten()):
            if idx >= num_feature_maps:
                ax.set_visible(False)
                continue

            feature_map = feature_maps[idx]
            ax.plot(feature_map.cpu().detach(), "b-")
            ax.set_title(f"{layer_name}: {idx}")
        plt.show()

    def plot_specific_feature_map(
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
            None
        """
        feature_map = super().get_specific_feature_map(layer_name, idx_kernel, input_ts).squeeze()

        plt.plot(feature_map.cpu().detach(), "b-")
        plt.title(f"{layer_name}: {idx_kernel}")
        plt.show()
