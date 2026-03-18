def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        means = [sum(el) / len(el) for el in zip(*matrix)]
    else:
        means = [sum(el) / len(el) for el in matrix]
    return means