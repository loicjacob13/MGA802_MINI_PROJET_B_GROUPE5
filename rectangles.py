"""
MGA802 - Mini-Projet B
Auteurs: Loïc Jacob, Fabien Koch, Guillaume Pissang

Description:
Module d'intégration numérique par la méthode des rectangles (point milieu).
On calcule l'aire sous la courbe d'une fonction polynomiale du 3e ordre :
    f(x) = p1 + p2*x + p3*x^2 + p4*x^3
sur l'intervalle [a, b] divisé en n segments réguliers.

Objectifs:
    - Implémenter la méthode des rectangles en Python de base (section 2.1.1)
    - Implémenter la même méthode en version vectorisée avec NumPy (section 2.1.2)
    - Calculer l'erreur par rapport à la solution analytique exacte
    - Étudier la convergence en fonction du nombre de segments n
    - Comparer les temps d'exécution des deux implémentations avec timeit
"""

import numpy as np  # importation de NumPy pour la version vectorisée (séance 5)

# ─────────────────────────────────────────────────────────────────
# CONSTANTES — paramètres par défaut du polynôme et de l'intervalle
# ─────────────────────────────────────────────────────────────────

# Paramètres du polynôme f(x) = p1 + p2*x + p3*x^2 + p4*x^3
P1_DEFAUT = 2.0  # terme constant
P2_DEFAUT = 1.0  # coefficient de x
P3_DEFAUT = -3.0  # coefficient de x^2
P4_DEFAUT = 0.5  # coefficient de x^3

A_DEFAUT = 0.0  # borne inférieure de l'intervalle d'intégration
B_DEFAUT = 3.0  # borne supérieure de l'intervalle d'intégration
N_DEFAUT = 10  # nombre de segments (valeur initiale de l'énoncé)


# ─────────────────────────────────────────────────────────────────
# FONCTIONS COMMUNES (Python de base)
# ─────────────────────────────────────────────────────────────────

def polynome(x, p1, p2, p3, p4):
    """
    Évalue le polynôme du 3e ordre f(x) = p1 + p2*x + p3*x^2 + p4*x^3 en x.

    Paramètres
    ----------
    x  : float ou np.ndarray — point(s) où évaluer le polynôme
    p1 : float — terme constant
    p2 : float — coefficient de x
    p3 : float — coefficient de x^2
    p4 : float — coefficient de x^3

    Retourne
    --------
    float ou np.ndarray — valeur(s) de f en x
    """
    return p1 + p2 * x + p3 * x ** 2 + p4 * x ** 3  # formule directe du polynôme


def integrale_analytique(a, b, p1, p2, p3, p4):
    """
    Calcule la solution exacte de l'intégrale de f sur [a, b] en utilisant la
    primitive F(x) = p1*x + p2*x^2/2 + p3*x^3/3 + p4*x^4/4.

    La valeur exacte sert de référence pour évaluer la précision des méthodes
    numériques : I_exact = F(b) - F(a).

    Paramètres
    ----------
    a, b       : float — bornes de l'intervalle d'intégration
    p1–p4      : float — coefficients du polynôme

    Retourne
    --------
    float — valeur exacte de l'intégrale
    """

    def primitive(x):
        # Primitive du polynôme, calculée terme par terme
        return p1 * x + p2 * x ** 2 / 2 + p3 * x ** 3 / 3 + p4 * x ** 4 / 4

    return primitive(b) - primitive(a)  # théorème fondamental du calcul intégral


# ─────────────────────────────────────────────────────────────────
# SECTION 2.1.1 — MÉTHODE DES RECTANGLES EN PYTHON DE BASE
# ─────────────────────────────────────────────────────────────────

def rectangles_python(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode des rectangles (Python de base).

    Principe : on divise [a, b] en n segments de largeur h = (b-a)/n.
    La fonction est évaluée au CENTRE de chaque segment (point milieu),
    ce qui constitue un rectangle. L'intégrale approchée est la somme
    des aires de ces n rectangles.

        I_rect = h * Σ f(a + (i + 0.5) * h)   pour i = 0, 1, ..., n-1

    Version Python de base : uniquement des boucles for et des opérations
    scalaires, sans utiliser NumPy.

    Paramètres
    ----------
    a, b  : float — bornes de l'intervalle
    n     : int   — nombre de segments (plus n est grand, plus c'est précis)
    p1–p4 : float — coefficients du polynôme

    Retourne
    --------
    float — approximation numérique de l'intégrale
    """
    h = (b - a) / n  # largeur de chaque segment (pas d'intégration)
    total = 0.0  # initialisation de la somme des aires des rectangles

    for i in range(n):
        # x_milieu est le centre du i-ème segment [a + i*h, a + (i+1)*h]
        x_milieu = a + (i + 0.5) * h

        # on ajoute l'aire du rectangle : hauteur f(x_milieu) × largeur h
        total = total + polynome(x_milieu, p1, p2, p3, p4) * h

    return total  # somme totale = approximation de l'intégrale


def erreur_rectangles_python(a, b, n, p1, p2, p3, p4):
    """
    Calcule l'erreur absolue entre la méthode des rectangles (Python de base)
    et la solution analytique exacte.

        erreur = |I_rect - I_exact|

    Paramètres
    ----------
    a, b  : float — bornes de l'intervalle
    n     : int   — nombre de segments
    p1–p4 : float — coefficients du polynôme

    Retourne
    --------
    float — erreur absolue
    """
    i_exact = integrale_analytique(a, b, p1, p2, p3, p4)  # solution de référence
    i_approx = rectangles_python(a, b, n, p1, p2, p3, p4)  # approximation numérique
    return abs(i_approx - i_exact)  # erreur absolue


def convergence_python(a, b, liste_n, p1, p2, p3, p4):
    """
    Retourne l'erreur de la méthode des rectangles (Python de base) pour
    chaque valeur de n fournie dans liste_n.

    Cette fonction permet d'étudier la convergence de la méthode :
    à mesure que n augmente, l'erreur doit diminuer.

    Paramètres
    ----------
    a, b    : float      — bornes de l'intervalle
    liste_n : list[int]  — liste des nombres de segments à tester
    p1–p4   : float      — coefficients du polynôme

    Retourne
    --------
    list[float] — liste des erreurs correspondant à chaque valeur de n
    """
    liste_erreurs = []  # liste vide pour stocker les erreurs calculées

    for n in liste_n:
        # on calcule et stocke l'erreur pour ce nombre de segments
        erreur = erreur_rectangles_python(a, b, n, p1, p2, p3, p4)
        liste_erreurs.append(erreur)

    return liste_erreurs  # on retourne toutes les erreurs dans le même ordre que liste_n


# ─────────────────────────────────────────────────────────────────
# SECTION 2.1.2 — MÉTHODE DES RECTANGLES AVEC NUMPY (VECTORISÉE)
# ─────────────────────────────────────────────────────────────────

def rectangles_numpy(a, b, n, p1, p2, p3, p4):
    """
    Intégration numérique par la méthode des rectangles (version NumPy vectorisée).

    Même principe que rectangles_python(), mais toute la boucle for est remplacée
    par des opérations vectorielles NumPy, ce qui est beaucoup plus rapide sur de
    grands nombres de segments.

    Étapes :
        1. np.linspace crée le tableau des n centres de segments en une seule ligne
        2. polynome() évalue f simultanément sur tous les centres (vectorisation)
        3. np.sum fait la somme de toutes les valeurs en une opération

    Paramètres
    ----------
    a, b  : float — bornes de l'intervalle
    n     : int   — nombre de segments
    p1–p4 : float — coefficients du polynôme

    Retourne
    --------
    float — approximation numérique de l'intégrale
    """
    h = (b - a) / n  # largeur de chaque segment (identique à la version Python)

    # np.linspace génère le tableau des n centres de segments :
    # [a + 0.5*h, a + 1.5*h, ..., a + (n-0.5)*h]
    # on utilise linspace(a + h/2, b - h/2, n) pour avoir exactement les milieux
    centres = np.linspace(a + h / 2, b - h / 2, n)  # tableau 1D de n points

    # évaluation vectorisée : polynome() reçoit un ndarray et retourne un ndarray
    # (la fonction polynome est compatible NumPy car elle n'utilise que +, *, ** )
    valeurs = polynome(centres, p1, p2, p3, p4)  # tableau des f(x_milieu_i)

    # np.sum additionne toutes les valeurs du tableau en une seule opération
    return h * np.sum(valeurs)  # I_rect ≈ h × Σ f(x_milieu_i)


def erreur_rectangles_numpy(a, b, n, p1, p2, p3, p4):
    """
    Calcule l'erreur absolue entre la méthode des rectangles (NumPy)
    et la solution analytique exacte.

    Paramètres
    ----------
    a, b  : float — bornes de l'intervalle
    n     : int   — nombre de segments
    p1–p4 : float — coefficients du polynôme

    Retourne
    --------
    float — erreur absolue
    """
    i_exact = integrale_analytique(a, b, p1, p2, p3, p4)  # solution de référence
    i_approx = rectangles_numpy(a, b, n, p1, p2, p3, p4)  # approximation NumPy
    return abs(i_approx - i_exact)  # erreur absolue


def convergence_numpy(a, b, liste_n, p1, p2, p3, p4):
    """
    Retourne l'erreur de la méthode des rectangles (NumPy) pour chaque valeur
    de n fournie dans liste_n. Même logique que convergence_python() mais
    en utilisant la version vectorisée.

    Paramètres
    ----------
    a, b    : float      — bornes de l'intervalle
    liste_n : list[int]  — liste des nombres de segments à tester
    p1–p4   : float      — coefficients du polynôme

    Retourne
    --------
    list[float] — liste des erreurs correspondant à chaque valeur de n
    """
    liste_erreurs = []  # liste vide pour stocker les erreurs calculées

    for n in liste_n:
        # on calcule et stocke l'erreur pour ce nombre de segments
        erreur = erreur_rectangles_numpy(a, b, n, p1, p2, p3, p4)
        liste_erreurs.append(erreur)

    return liste_erreurs  # on retourne toutes les erreurs dans le même ordre que liste_n