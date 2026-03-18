import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	a = np.array(a)
	if np.prod(a.shape) != np.prod(new_shape):
		return []
	reshaped_matrix = a.reshape(new_shape)
	return reshaped_matrix