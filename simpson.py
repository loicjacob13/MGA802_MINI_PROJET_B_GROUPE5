import numpy as np

def polynome(x, p1, p2, p3, p4):
    """Évalue le polynôme du 3e ordre en x."""
    return p1 + p2 * x + p3 * x**2 + p4 * x**3


# Méthode de Simpson — Python de base

def simpson_python(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode de Simpson (Python de base)
    """
    if n % 2 != 0:
        n -= 1  # Simpson nécessite un nombre pair de segments

    h = (b-a) / n #largeur d'un segment
    total = polynome(a, p1, p2, p3, p4) + polynome(b, p1, p2, p3, p4) #on initialise avec les deux bornes

    for i in range(1, n): #on parcourt les points intérieurs (sans les bornes)
        xi = a + i * h
        if i % 2 == 0:
            total += 2 * polynome(xi, p1, p2, p3, p4) #indices pairs -> coefficient 2
        else:
            total += 4 * polynome(xi, p1, p2, p3, p4) #indices impairs -> coefficient 4

    return total * h / 3 #formule de Simpson : somme * h/3

# Méthode de Simpson — NumPy (vectorisé)

def simpson_numpy(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode de Simpson (NumPy vectorisé).
    """
    if n % 2 != 0:
        n -= 1 #même contrainte que la version python

    x = np.linspace(a, b, n + 1) # n+1 points réguliers, n segments sur [a,b]
    y = polynome(x, p1, p2, p3, p4) # évaluation vectorisée du polynôme sur tous les points


    # Coefficients de Simpson : 1, 4, 2, 4, 2, ..., 4, 1
    coeffs = np.ones(n + 1)
    coeffs[1:-1:2] = 4   # indices impairs -> 4
    coeffs[2:-2:2] = 2   # indices pairs intérieurs -> 2

    h = (b - a) / n
    return np.dot(coeffs, y) * h/3 #produit scalaire remplace la boucle for


