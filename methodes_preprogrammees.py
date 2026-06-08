import numpy as np
from scipy.integrate import trapezoid, simpson

def polynome(x, p1, p2, p3, p4):
    """Évalue le polynôme du 3e ordre en x (scalaire ou tableau NumPy)."""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

def trapezes_scipy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la méthode des trapèzes via scipy.integrate.trapezoid.
    """
    x = np.linspace(a, b, n + 1)
    y = polynome(x, p1, p2, p3, p4)
    return float(trapezoid(y, x))


def simpson_scipy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la méthode de Simpson via scipy.integrate.simpson.
    """
    if n % 2 != 0:
        n += 1  # on arrondit vers le haut pour ne pas perdre de précision
    x = np.linspace(a, b, n + 1)
    y = polynome(x, p1, p2, p3, p4)
    return float(simpson(y, x=x))
