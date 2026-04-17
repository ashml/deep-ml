import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    batches = []
    n = X.shape[0]
    for i in range(0, n, batch_size):
        batch = [X[i:i+batch_size]]
        if y is not None:
            batch.append(y[i:i+batch_size])
        batches.append(batch)
    return batches