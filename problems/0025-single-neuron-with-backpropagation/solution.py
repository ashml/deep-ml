import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    mse_values = []
    for _ in range(epochs):
        z = features @ initial_weights + initial_bias
        y_pred = 1 / (1 + np.exp(-z))
        mse = np.mean((labels - y_pred) ** 2)
        mse_values.append(round(mse, 4))

        dz = 2 * (y_pred - labels) * y_pred * (1 - y_pred)

        dw = features.T @ dz / len(labels)
        db = np.mean(dz)

        initial_weights -= learning_rate * dw
        initial_bias -= learning_rate * db

    initial_weights = np.round(initial_weights, 4)
    initial_bias = round(initial_bias, 4)

    return initial_weights, initial_bias, mse_values