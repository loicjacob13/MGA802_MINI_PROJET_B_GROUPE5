import numpy as np
from scipy.integrate import trapezoid, simpson

def polynome(x, p1, p2, p3, p4):
    """Évalue le polynôme du 3e ordre en x (scalaire ou tableau NumPy)."""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

def trapezes_scipy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la méthode des trapèzes via scipy.integrate.trapezoid.
    """
    x = np.linspace(a, b, n + 1) #n+1 points réguliers pour délimiter n segments
    y = polynome(x, p1, p2, p3, p4) #évaluation vectorisée du polynôme sur tous les points
    return float(trapezoid(y, x)) #scipy calcule la somme des trapèzes directement

def simpson_scipy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la méthode de Simpson via scipy.integrate.simpson.
    """
    if n % 2 != 0:
        n += 1  # on arrondit vers le haut pour ne pas perdre de précision
    x = np.linspace(a, b, n + 1) #n+1 points réguliers
    y = polynome(x, p1, p2, p3, p4) #évaluation vectorisée
    return float(simpson(y, x=x)) #x=x précise l'axe des abscisses à scipy
