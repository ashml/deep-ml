import numpy as np

def precision(y_true, y_pred):
    tp = sum((y_true == y_pred) & (y_true == 1))
    fp = sum((y_true != y_pred) & (y_pred == 1))
    return tp / (tp + fp)