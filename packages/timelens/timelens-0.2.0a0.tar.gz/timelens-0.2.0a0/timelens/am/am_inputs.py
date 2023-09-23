import numpy as np


def zero_ts(c, t):
    """Returns a 3-D array which is initialzed with zero.

    Args:
        c (int): the number of sensors (C).
        t (int): length of the input signal (T)

    Returns:
        np.ndarray: 3-D array with shape [N(=1), C, T]

    """
    x_zeros = np.zeros((1, c, t))
    return x_zeros


def square_ts(c, t, vmax, freq):
    """Returns a 3-D array which is initialized by square wave.

    In the 2rd dimension, each signal is initialized with the same time series.

    Output array has [min, max] = [-vmax, +vmax].

    Args:
        c (int): the number of channels (C)
        t (int): length of the input signal (T)
        vmax (float): maximum amplitude
        freq (float): frequency of square wave

    Returns:
        np.ndarray: square wave, a 3-D array with shape [N(=1), C, T]

    """
    x_sq = np.zeros(t)
    interval = int(t / (2 * freq))
    sign = 1
    for i in range(0, t, interval):
        x_sq[i:i + interval] = sign
        sign *= -1
    x_sq = x_sq.reshape(1, 1, t) * vmax
    return np.concatenate([x_sq] * c, axis=1)


def noise_ts(c, t, vmax):
    """Returns a 3-D array which is initialzed with white noise.

    In the 2rd dimension, each signal is initialized with the same time series.

    Output array has [min, max] = [-vmax, +vmax].

    Args:
        c (int): the number of channels (C)
        t (int): length of the input signal (T)
        vmax (float): maximum amplitude

    Returns:
        np.ndarray: a 3-D array with shape [N(=1), C, T]

    """
    x_rand = np.random.rand(t)
    x_rand = (x_rand - x_rand.min()) / (x_rand.max() - x_rand.min())
    x_rand = ((x_rand - 0.5) * 2).reshape(1, 1, t) * vmax
    return np.concatenate([x_rand] * c, axis=1)


def sin_ts(c, t, vmax, freq):
    """Returns a 3-D array which is initialized by sin wave.

    In the 2rd dimension, each signal is initialized with the same time series.

    Output array has [min, max] = [-vmax, +vmax].

    Args:
        c (int): the number of channels (C)
        t (int): length of the input signal (T)
        vmax (float): maximum amplitude
        freq (float): frequency of sin wave

    Returns:
        np.ndarray: sin wave, a 3-D array with shape [N(=1), C, T]

    """
    duration = int(t / 30)
    rad_end = int((2 * np.pi * freq)) * duration
    x_sin = np.sin(np.linspace(0, rad_end, t)).reshape(1, 1, t) * vmax
    return np.concatenate([x_sin] * c, axis=1)


def triangle_ts(c, t, vmax, freq):
    """Returns a 3-D array which is initialized by triangle wave.

    In the 2rd dimension, each signal is initialized with the same time series.

    Output array has [min, max] = [-vmax, +vmax].

    Args:
        c (int): the number of channels (C)
        t (int): length of the input signal (T)
        vmax (float): maximum amplitude
        freq (float): frequency of triangle wave

    Returns:
        np.ndarray: triangle wave, a 3-D array with shape [N(=1), Ch(=1), T]

    """
    interval = int(np.ceil(t / freq))
    slope = 2.0 / interval
    x_tri = []
    for direction, alpha in [(1, 0), (-1, 0.5), (-1, 0), (1, -0.5)]:
        x_tri.append(direction * slope * np.arange(int(np.ceil(interval / 4)), dtype=np.float64) + alpha)
    x_tri = np.stack(x_tri, axis=0)
    x_tri = np.array([x_tri] * int(np.ceil(freq))).ravel()
    x_tri = x_tri[:t].reshape(1, 1, t) * 2.0 * vmax
    return np.concatenate([x_tri] * c, axis=1)
