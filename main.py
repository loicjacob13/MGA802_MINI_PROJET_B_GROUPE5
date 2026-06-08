from solution_analytique import fonction_polynome, solution_analytique
from fonction_erreur import fonction_erreur
from rectangles import rectangles_python, rectangles_numpy
from trapezes import integration_trapezes, integration_trapezes_numpy
from simpson import simpson_python, simpson_numpy
from saisie_utilisateur import demander_bornes, demander_entier_positif, demander_coefficients


if __name__ == "__main__":
    print("veuillez saisir les paramètres de l'intégration: ")

    #coefficients du polynôme
    p1,p2,p3,p4=demander_coefficients()

    #bornes d'intégration
    a,b = demander_bornes()

    #nombre de segments
    n=demander_entier_positif("nombre de segments n: ")

    #solution analytique de l'intégrale
    valeur_exacte=solution_analytique(a,b,p1,p2,p3,p4)


#calcul des intégrales en utilisant les 3 différentes modèles
    #2 méthodes pour chaque : méthode simple python de base, et méthode numpy

    #méthode des rectangles
    aire_rect_python = rectangles_python(a, b, n, p1, p2, p3, p4)
    aire_rect_numpy = rectangles_numpy(a, b, n, p1, p2, p3, p4)

    # méthode des trapèzes
    aire_trap_python = integration_trapezes_python(a, b, n, p1, p2, p3, p4)
    aire_trap_numpy = integration_trapezes(a, b, n, p1, p2, p3, p4)

    # méthode de Simpson
    aire_simp_python = simpson_python(a, b, n, p1, p2, p3, p4)
    aire_simp_numpy = simpson_numpy(a, b, n, p1, p2, p3, p4)

#calcul des erreurs analytique - numérique

    erreur_rect_python = calculer_erreur(aire_rect_python, valeur_exacte)
    erreur_rect_numpy = calculer_erreur(aire_rect_numpy, valeur_exacte)

    erreur_trap_python = calculer_erreur(aire_trap_python, valeur_exacte)
    erreur_trap_numpy = calculer_erreur(aire_trap_numpy, valeur_exacte)

    erreur_simp_python = calculer_erreur(aire_simp_python, valeur_exacte)
    erreur_simp_numpy = calculer_erreur(aire_simp_numpy, valeur_exacte)


#Résultats
    print(f"voci votre polynôme : f(x) = {p1} + {p2}x + {p3}x^2 + {p4}x^3")
    print(f"intervalle : [{a}, {b}]   ,   nombre de segments : n = {n}")
    print(f"Valeur exacte (analytique) : {valeur_exacte}")

    #méthode rectangle
    print("MÉTHODE DES RECTANGLES")
    print(f"  Python : aire = {aire_rect_python:.10f}   erreur = {erreur_rect_python:.2e}")#.10f --> 10 décimales, .2e format exponentielle avec 2 décimales
    print(f"  NumPy  : aire = {aire_rect_numpy:.10f}   erreur = {erreur_rect_numpy:.2e}")

    #méthode des trapèzes
    print("MÉTHODE DES TRAPÈZES")
    print(f"  Python : aire = {aire_trap_python:.10f}   erreur = {erreur_trap_python:.2e}")
    print(f"  NumPy  : aire = {aire_trap_numpy:.10f}   erreur = {erreur_trap_numpy:.2e}")

    #méthode simpson
    print("MÉTHODE DE SIMPSON")
    print(f"  Python : aire = {aire_simp_python:.10f}   erreur = {erreur_simp_python:.2e}")
    print(f"  NumPy  : aire = {aire_simp_numpy:.10f}   erreur = {erreur_simp_numpy:.2e}")

