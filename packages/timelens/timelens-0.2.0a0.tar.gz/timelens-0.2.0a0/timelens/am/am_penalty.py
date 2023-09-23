import torch


def l2_norm(x):
    """ Implementation of L2 norm penalty

    Args:
        x (torch.Tensor): input tensor with shape = [1, S, T]

    Returns:
        l2_norm penalty (float): Penalty term for L2 norm
    """
    return torch.sqrt(torch.sum(x**2))


def total_variation(x):
    """ Implementation of Total Variation (TV) penalty

    Args:
        x (torch.Tensor): input tensor with shape = [1, S, T]

    Returns:
        tv_norm penalty (float): Penalty term for total variation
    """
    x1 = x[:, :, 1:]
    x2 = x[:, :, :-1]
    return torch.sum(torch.abs(x1 - x2))


def extreme_value_penalty(acts, th):
    """ Implementation of extreme value penalty (EAP)

    Args:
        acts (torch.Tensor): input tensor with activations | Shape: (1, S, T)
        th (float): threshold. This value is defined by a 2-sigma/3-sigma rule.

    Returns:
        eap_norm penalty: Penalty term for extreme value penalty
    """
    acts_flattend = torch.abs(acts).view(-1) - th
    acts_anorm = acts_flattend[acts_flattend > 0]
    if len(acts_anorm) == 0:
        return torch.tensor(0.)
    return torch.mean(acts_anorm)


