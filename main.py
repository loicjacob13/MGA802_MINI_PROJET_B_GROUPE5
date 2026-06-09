"""
MGA802 - Mini-Projet B
Auteurs: Loïc Jacob (JACL93280301) ; Fabien Koch (KOCF83320301) ; Guillaume Pissang (PISG89300201)

Point d'entrée principal du programme.
- Demande à l'utilisateur les paramètres du polynôme, les bornes et le nombre de segments
- Calcule l'intégrale par 8 méthodes (rectangles, trapèzes, Simpson en Python/NumPy/SciPy)
- Affiche les résultats et les erreurs par rapport à la solution analytique exacte
- Trace les graphiques de convergence et de temps de calcul
- Lance le benchmark perf_counter et timeit sur toutes les méthodes
"""

from solution_analytique import solution_analytique
from fonction_erreur import calculer_erreur
from rectangles import rectangles_python, rectangles_numpy
from trapezes import integration_trapezes_python, integration_trapezes
from simpson import simpson_python, simpson_numpy
from saisie_utilisateur import demander_bornes, demander_entier_positif, demander_coefficients
from analyse import convergence, generer_liste_n,tracer_convergence, temps_selon_n, tracer_temps
from methodes_preprogrammees import trapezes_scipy, simpson_scipy

from benchmark_projet_B import benchmark_perf_counter, benchmark_timeit


if __name__ == "__main__":
    print("veuillez saisir les paramètres de l'intégration: ")

    #coefficients du polynôme
    p1,p2,p3,p4=demander_coefficients()

    #bornes d'intégration
    a,b = demander_bornes()

    #nombre de segments
    n=demander_entier_positif("nombre de segments n: ")

    # solution analytique (valeur exacte de l'intégrale qui servira de référence)
    valeur_exacte = solution_analytique(a, b, p1, p2, p3, p4)

#étude de la convergence de la solution selon le nombre de segments n
    # on génère automatiquement la liste des n à tester (10, 20, 40, ... )
    liste_n = generer_liste_n()

    #on va calculer l'erreur pour chaque méthode sur toute la liste de n
    erreurs_rect_python = convergence(rectangles_python, a, b, liste_n, p1, p2, p3, p4, valeur_exacte)
    erreurs_rect_numpy = convergence(rectangles_numpy, a, b, liste_n, p1, p2, p3, p4, valeur_exacte)
    erreurs_trap_python = convergence(integration_trapezes_python, a, b, liste_n, p1, p2, p3, p4, valeur_exacte)
    erreurs_trap_numpy = convergence(integration_trapezes, a, b, liste_n, p1, p2, p3, p4, valeur_exacte)
    erreurs_simp_python = convergence(simpson_python, a, b, liste_n, p1, p2, p3, p4, valeur_exacte)
    erreurs_simp_numpy = convergence(simpson_numpy, a, b, liste_n, p1, p2, p3, p4, valeur_exacte)

#graphique de convergence (erreur vs n), on se sert du dictionnaire explicité dans le module analyse.py
    # chaque valeur du dictionnaire renvoie une liste, une erreur par valeur de n
    dictionnaire_erreurs = {
        "Rectangles": erreurs_rect_python,
        "Trapèzes": erreurs_trap_python,
        "Simpson": erreurs_simp_python,
    }
    tracer_convergence(liste_n, dictionnaire_erreurs)
    


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

    # méthode des trapèzes SciPy
    aire_trap_scipy = trapezes_scipy(a, b, n, p1, p2, p3, p4)

    # méthode de Simpson SciPy
    aire_simp_scipy = simpson_scipy(a, b, n, p1, p2, p3, p4)

#calcul des erreurs analytique - numérique

    erreur_rect_python = calculer_erreur(aire_rect_python, valeur_exacte)
    erreur_rect_numpy = calculer_erreur(aire_rect_numpy, valeur_exacte)

    erreur_trap_python = calculer_erreur(aire_trap_python, valeur_exacte)
    erreur_trap_numpy = calculer_erreur(aire_trap_numpy, valeur_exacte)

    erreur_simp_python = calculer_erreur(aire_simp_python, valeur_exacte)
    erreur_simp_numpy = calculer_erreur(aire_simp_numpy, valeur_exacte)

    erreur_trap_scipy = calculer_erreur(aire_trap_scipy, valeur_exacte)
    erreur_simp_scipy = calculer_erreur(aire_simp_scipy, valeur_exacte)

    #Résultats
    print(f"\nVoici votre polynôme : f(x) = {p1} + {p2}x + {p3}x^2 + {p4}x^3")
    print(f"intervalle : [{a}, {b}]   ,   nombre de segments : n = {n}")
    print(f"La valeur exacte (analytique) est : {valeur_exacte}")

    #méthode rectangle
    print("\nMÉTHODE DES RECTANGLES")
    print(f"  Python : aire = {aire_rect_python:.10f}   erreur = {erreur_rect_python:.2e}")#.10f --> 10 décimales, .2e format exponentielle avec 2 décimales
    print(f"  NumPy  : aire = {aire_rect_numpy:.10f}   erreur = {erreur_rect_numpy:.2e}")

    #méthode des trapèzes
    print("\nMÉTHODE DES TRAPÈZES")
    print(f"  Python : aire = {aire_trap_python:.10f}   erreur = {erreur_trap_python:.2e}")
    print(f"  NumPy  : aire = {aire_trap_numpy:.10f}   erreur = {erreur_trap_numpy:.2e}")

    #méthode simpson
    print("\nMÉTHODE DE SIMPSON")
    print(f"  Python : aire = {aire_simp_python:.10f}   erreur = {erreur_simp_python:.2e}")
    print(f"  NumPy  : aire = {aire_simp_numpy:.10f}   erreur = {erreur_simp_numpy:.2e}")


    # méthodes pré-programmées (SciPy)
    print("\nMÉTHODES PRÉ-PROGRAMMÉES (SciPy)")
    print(f"  Trapèzes SciPy : aire = {aire_trap_scipy:.10f}   erreur = {erreur_trap_scipy:.2e}")
    print(f"  Simpson  SciPy : aire = {aire_simp_scipy:.10f}   erreur = {erreur_simp_scipy:.2e}")

    PARAMETRES = (a, b, n, p1, p2, p3, p4) #tuple des paramètres pour éviter de répéter les 7 arguments à chaque appel
    REPETITIONS = demander_entier_positif("\nnombre de répétitions pour le benchmark: ")

    # liste des méthodes : chaque entrée est (nom affiché, fonction à appeler)
    methodes = [
        ("Rectangles Python", rectangles_python),
        ("Rectangles NumPy ", rectangles_numpy),
        ("Trapèzes    Python", integration_trapezes_python),
        ("Trapèzes    NumPy ", integration_trapezes),
        ("Simpson     Python", simpson_python),
        ("Simpson     NumPy ", simpson_numpy),
        ("Trapèzes    SciPy ", trapezes_scipy),
        ("Simpson     SciPy ", simpson_scipy),
    ]

    print("\n" + "=" * 60)
    print("  BENCHMARK")
    print("=" * 60)
    benchmark_perf_counter(methodes, PARAMETRES, valeur_exacte) # une seule exécution par méthode
    benchmark_timeit(methodes, PARAMETRES, REPETITIONS) # moyenne sur N répétitions

#graphique du temps de calcul vs n
    dictionnaire_temps = {
        "Rectangles Python": temps_selon_n(rectangles_python, a, b, liste_n, p1, p2, p3, p4),
        "Rectangles NumPy": temps_selon_n(rectangles_numpy, a, b, liste_n, p1, p2, p3, p4),
        "Trapèzes Python": temps_selon_n(integration_trapezes_python, a, b, liste_n, p1, p2, p3, p4),
        "Trapèzes NumPy": temps_selon_n(integration_trapezes, a, b, liste_n, p1, p2, p3, p4),
        "Simpson Python": temps_selon_n(simpson_python, a, b, liste_n, p1, p2, p3, p4),
        "Simpson NumPy": temps_selon_n(simpson_numpy, a, b, liste_n, p1, p2, p3, p4),
    }
    tracer_temps(liste_n, dictionnaire_temps)


