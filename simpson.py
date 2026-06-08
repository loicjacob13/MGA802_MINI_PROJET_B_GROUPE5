import numpy as np

def polynome(x, p1, p2, p3, p4):
    """Évalue le polynôme du 3e ordre en x."""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3

def integrale_analytique(a, b, p1, p2, p3, p4):
    """
    Calcule l'intégrale exacte de f sur [a, b] :
        I = p1*x + p2*x^2/2 + p3*x^3/3 + p4*x^4/4
    """
    def primitive(x):
        return p1 * x + p2 * x**2 / 2 + p3 * x**3 / 3 + p4 * x**4 / 4
    return primitive(b) - primitive(a)

# Méthode de Simpson — Python de base

def simpson_python(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode de Simpson (Python de base)
    """
    if n % 2 != 0:
        n -= 1  # Simpson nécessite un nombre pair de segments

    h = (b-a) / n
    total = polynome(a, p1, p2, p3, p4) + polynome(b, p1, p2, p3, p4)

    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 0:
            total += 2 * polynome(xi, p1, p2, p3, p4)
        else:
            total += 4 * polynome(xi, p1, p2, p3, p4)

    return total * h / 3

# Méthode de Simpson — NumPy (vectorisé)

def simpson_numpy(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode de Simpson (NumPy vectorisé).
    """
    if n % 2 != 0:
        n -= 1

    x = np.linspace(a, b, n + 1)        # n+1 points, n segments
    y = polynome(x, p1, p2, p3, p4)

    # Coefficients de Simpson : 1, 4, 2, 4, 2, ..., 4, 1
    coeffs = np.ones(n + 1)
    coeffs[1:-1:2] = 4   # indices impairs -> 4
    coeffs[2:-2:2] = 2   # indices pairs intérieurs -> 2

    h = (b - a) / n
    return np.dot(coeffs, y) * h/3

# Calcul de l'erreur

def erreur_simpson(a, b, n, p1, p2, p3, p4, methode='numpy'):
    """
    Calcule l'erreur absolue entre la méthode de Simpson et la solution exacte.
    """
    exacte = integrale_analytique(a, b, p1, p2, p3, p4)
    if methode == 'python':
        approx = simpson_python(a, b, n, p1, p2, p3, p4)
    else:
        approx = simpson_numpy(a, b, n, p1, p2, p3, p4)
    return abs(approx - exacte)
