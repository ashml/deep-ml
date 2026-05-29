import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    p = np.array(p)
    q = np.array(q)
    if len(p) != len(q):
        return 0.0
    prod = p * q
    sqr = np.sqrt(prod)
    return -np.log(sum(sqr))