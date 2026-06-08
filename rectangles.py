"""
MGA802 - Mini-Projet B
Auteurs: Loïc Jacob, Fabien Koch, Guillaume Pissang

Description:
Module d'intégration numérique avec la méthode des rectangles (point milieu).
On calcule l'aire sous la courbe d'une fonction polynomiale du 3e ordre :
    f(x) = p1 + p2*x + p3*x^2 + p4*x^3
sur l'intervalle [a, b] divisé en n segments réguliers
La fonction est évaluée au centre de chaque segment, ce qui va former
n rectangles dont la somme des aires approche l'intégrale

Objectifs:
    - Implémenter la méthode des rectangles en Python de base
    - Implémenter la même méthode vectorisée avec NumPy
"""

import numpy as np  # importation de NumPy pour la version vectorisée


def polynome(x, p1, p2, p3, p4):
    """Évalue le polynôme du 3e ordre en x"""
    return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3

# Méthode des rectangles — Python de base

def rectangles_python(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode des rectangles (Python de base)

    Principe : l'intervalle [a, b] est divisé en n segments de largeur h = (b-a)/n
    La fonction est évaluée au CENTRE de chaque segment (point milieu x_i + h/2),
    ce qui forme un rectangle. L'intégrale est approchée par la somme des n aires
    """
    h = (b - a) / n  # largeur de chaque segment (pas d'intégration)
    total = 0.0  # initialisation de la somme des aires

    for i in range(n):
        x_milieu = a + (i + 0.5) * h  # centre du i-ème segment
        total += polynome(x_milieu, p1, p2, p3, p4) * h  # aire du rectangle i
    return total


# Méthode des rectangles — NumPy (vectorisé)

def rectangles_numpy(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode des rectangles (NumPy vectorisé)

    Même principe que rectangles_python(), mais la boucle for est remplacée par
    des opérations vectorielles NumPy vues en cours :
        - np.linspace génère tous les centres de segments en une seule ligne
        - polynome() évalue f sur tout le tableau d'un coup
        - np.sum additionne toutes les aires sans boucle explicite
    """
    h = (b - a) / n  # largeur de chaque segment
    centres = np.linspace(a + h / 2, b - h / 2, n)    # np.linspace génère le tableau des n centres : [a+h/2, a+3h/2, ..., b-h/2]
    valeurs = polynome(centres, p1, p2, p3, p4)     # évaluation vectorisée : polynome reçoit un ndarray et retourne un ndarray
    return h * np.sum(valeurs)
