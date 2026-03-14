import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    def evaluate(poly, x):
        result = 0
        n = len(poly)
        for i, coef in enumerate(poly):
            result += coef * (x ** (n - i - 1))
        return result

    def derivative(poly):
        n = len(poly)
        return [(n - i - 1) * poly[i] for i in range(n - 1)]

    g_val = evaluate(g_coeffs, x)
    h_val = evaluate(h_coeffs, x)
    g_prime_val = evaluate(derivative(g_coeffs), x)
    h_prime_val = evaluate(derivative(h_coeffs), x)
    f_prime_val = (g_prime_val * h_val - g_val * h_prime_val) / (h_val ** 2)
    return f_prime_val