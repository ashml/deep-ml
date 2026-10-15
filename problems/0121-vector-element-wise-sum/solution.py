import numpy as np

def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    if len(a) != len(b):
        return -1
    
    a = np.array(a)
    b = np.array(b)
    return a + b