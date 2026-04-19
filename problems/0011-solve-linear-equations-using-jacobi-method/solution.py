import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    m = len(A)
    x = [0.0 for _ in range(m)]
    for _ in range(n):
        x_new = x.copy()
        for i in range(m):
            s = sum(A[i][j] * x[j] for j in range(m) if j != i)
            x_new[i] = round((b[i] - s) / A[i][i], 4)
        x = x_new
    return x