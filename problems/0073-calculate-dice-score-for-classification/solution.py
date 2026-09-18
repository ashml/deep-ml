import numpy as np

def dice_score(y_true, y_pred):
    n = sum(y_true) + sum(y_pred) + 0.000001
    intersection = np.sum((y_true == y_pred) & (y_true == 1))
    res = 2 * intersection / n
    return round(res, 3)