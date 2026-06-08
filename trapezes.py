def fonction_polynome(x, p1, p2, p3, p4):
    """renvoie la valeur du polynomiale du 3e ordre au point x.
    f(x) = p1 + p2*x + p3*x^2 + p4*x^3 (équation (1) de l'énoncé)"""
    valeur = p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3)
    return valeur


def integration_trapezes_python(a, b, n, p1, p2, p3, p4):
    """calcule l'intégrale de f entre a et b par la méthode des trapèzes,
    en Python de base (avec une boucle for et sans NumPy).

    a, b : bornes de l'intervalle d'intégration
    n    : nombre de segments
    p1, p2, p3, p4 : coefficients du polynôme

    Renvoie l'aire approximée sous la courbe."""

    largeur_segment = (b - a) / n  # largeur h d'un segment (tous identiques)
    aire_totale = 0  # on accumule l'aire des trapèzes au fur et à mesure

    # On parcourt chacun des n segments
    for i in range(n):
        x_gauche = a + i * largeur_segment  # borne gauche du segment courant
        x_droite = a + (i + 1) * largeur_segment  # borne droite du segment courant

        # On évalue la fonction aux deux bornes du segment
        f_gauche = fonction_polynome(x_gauche, p1, p2, p3, p4) #appel de la fonction polynome pour renvoyer la valeur
        f_droite = fonction_polynome(x_droite, p1, p2, p3, p4)

        # Aire du trapèze sur ce segment : T = (b - a) * (f(a) + f(b)) / 2  (équation (2))
        aire_trapeze = largeur_segment * (f_gauche + f_droite) / 2

        # On ajoute l'aire de ce trapèze à l'aire totale
        aire_totale = aire_totale + aire_trapeze

    return aire_totale