
import numpy as np

def jaccard_index(y_true, y_pred):
    intersection = np.sum(y_true + y_pred > 1)
    union = np.sum(y_true + y_pred >= 1)
    return round(intersection / union, 3)