def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = [[el * scalar for el in row] for row in matrix]
	return result