
import numpy as np

def gini_impurity(y):
    if len(y) == 0:
        return 0.0

    n = len(y)
    gini = 1.0

    for cls in set(y):
        p = y.count(cls) / n
        gini -= p ** 2

    return gini