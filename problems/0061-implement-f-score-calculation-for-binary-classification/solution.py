import numpy as np

def f_score(y_true, y_pred, beta):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    tp = sum((y_true == 1) & (y_true == y_pred))
    fp = sum((y_true == 0) & (y_true != y_pred))
    fn = sum((y_true == 1) & (y_true != y_pred))

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    fbeta = (1 + beta**2) * ((precision * recall) / (beta**2 * precision + recall))

    return round(fbeta, 3)
