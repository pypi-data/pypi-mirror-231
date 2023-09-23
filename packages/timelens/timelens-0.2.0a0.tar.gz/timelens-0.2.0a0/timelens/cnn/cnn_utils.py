import torch


def normalize_kernel(kernel: torch.tensor, agg=True):
    # normalize filters to range of 0 to 1
    kernel = kernel - kernel.min()
    kernel = kernel / kernel.max()

    # aggregate all channels of a kernel using a linear combination with same weights
    if agg:
        factors = kernel.sum(axis=1) / kernel.sum()
        kernel = (factors @ kernel).reshape(1, kernel.size(-1))

    return kernel
