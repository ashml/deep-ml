import numpy as np


def poisson_deviance(y: np.ndarray, mu: np.ndarray) -> float:
    terms = np.where(y > 0, y * np.log(y / mu), 0)
    deviance = 2 * np.sum(terms - (y - mu))
    return float(deviance)


def dispersion_ratio(y: np.ndarray, mu: np.ndarray, n_params: int) -> float:
    n = len(y)
    pearson = np.sum((y - mu) ** 2 / mu)
    return float(pearson / (n - n_params))
