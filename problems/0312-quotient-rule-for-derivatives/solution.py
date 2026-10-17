import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    g = np.polyval(g_coeffs, x)
    h = np.polyval(h_coeffs, x)

    g_der = np.polyval(np.polyder(g_coeffs), x)
    h_der = np.polyval(np.polyder(h_coeffs), x)

    return float((g_der * h - g * h_der) / h**2)