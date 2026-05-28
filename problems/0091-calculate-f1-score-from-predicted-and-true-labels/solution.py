import numpy as np

def calculate_f1_score(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    tp = sum((y_true == 1) & (y_true == y_pred))
    fp = sum((y_true == 0) & (y_true != y_pred))
    fn = sum((y_true == 1) & (y_true != y_pred))

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    f1 = (2 * precision * recall) / (precision + recall)
    return round(f1 if f1 > 0 else 0, 3)