import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    def derivative(poly):
        return [i * poly[i] for i in range(1, len(poly))] or [0.0]

    def multiply(p1, p2):
        res = [0.0] * (len(p1) + len(p2) - 1)
        for i, a in enumerate(p1):
            for j, b in enumerate(p2):
                res[i + j] += a * b
        return res

    f_prime = derivative(f_coeffs)
    g_prime = derivative(g_coeffs)

    term1 = multiply(f_prime, g_coeffs)
    term2 = multiply(f_coeffs, g_prime)

    max_len = max(len(term1), len(term2))
    result = [round((term1[i] if i < len(term1) else 0) + 
                    (term2[i] if i < len(term2) else 0), 4)
              for i in range(max_len)]

    while len(result) > 1 and abs(result[-1]) < 1e-10:
        result.pop()

    return result