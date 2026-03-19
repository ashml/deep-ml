def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a, b = matrix[0]
    c, d = matrix[1]
    
    det = a * d - b * c
    if det == 0:
        return None

    inv_matrix = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
    return inv_matrix