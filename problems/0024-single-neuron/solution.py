import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    X = np.array(features)
    y = np.array(labels)
    w = np.array(weights)

    z = X @ w + bias
    predictions = 1 / (1 + np.exp(-z))
    mse = np.mean((predictions - y) ** 2)

    return predictions, mse