import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    values = arr.ravel()
    if norm_type == "l1":
        return float(np.sum(np.abs(values)))
    else:
        return float(np.sqrt(np.sum(values ** 2)))