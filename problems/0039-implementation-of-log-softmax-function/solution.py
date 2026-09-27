import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    max_el = max(scores)
    sz = sum(np.e**(el - max_el) for el in scores)
    return np.array(np.log([np.e**(el - max_el) / sz for el in scores]))