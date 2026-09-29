def phi_corr(x: list[int], y: list[int]) -> float:
    a = b = c = d = 0

    for xi, yi in zip(x, y):
        if xi == 1 and yi == 1:
            a += 1
        elif xi == 1 and yi == 0:
            b += 1
        elif xi == 0 and yi == 1:
            c += 1
        elif xi == 0 and yi == 0:
            d += 1

    val = (a * d - b * c) / ((a + b) * (c + d) * (a + c) * (b + d) + 0.0000000000001)**0.5

    return round(val, 4)