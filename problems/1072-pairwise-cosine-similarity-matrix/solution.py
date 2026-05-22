import numpy as np

def pairwise_cosine_similarity(X):
    X = np.array(X)
    norms = np.linalg.norm(X, axis=1)
    return np.nan_to_num((X @ X.T) / (np.outer(norms, norms)), nan=0.0)