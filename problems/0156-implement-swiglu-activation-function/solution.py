import numpy as np

def SwiGLU(x: np.ndarray) -> np.ndarray:
    """
    Args:
        x: np.ndarray of shape (batch_size, 2d)
    Returns:
        np.ndarray of shape (batch_size, d)
    """
    d = x.shape[-1] // 2
    x1 = x[:, :d]
    x2 = x[:, d:]

    sigmoid = 1 / (1 + np.exp(-x2))
    swish = x2 * sigmoid
    out = x1 * swish
    return np.round(out, 4)