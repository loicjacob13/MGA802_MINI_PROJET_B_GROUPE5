"""
MGA802 - Mini-Projet B
Script de perf_counter & time_it
Mesure les temps d'exécution des méthodes d'intégration numérique
"""

from time import perf_counter
from timeit import timeit

from rectangles import rectangles_python, rectangles_numpy
from trapezes import integration_trapezes_python, integration_trapezes
from simpson import simpson_python, simpson_numpy
from solution_analytique import solution_analytique
from fonction_erreur import calculer_erreur

# ── Paramètres ────────────────────────────────────────────────
a, b       = -2, 3          # bornes d'intégration
p1, p2, p3, p4 = 1, 2, -1, 0.5  # coefficients du polynôme de degré 3
N          = 1000           # nombre de segments
REPETITIONS = 100           # nombre de répétitions timeit

PARAMETRES = (a, b, N, p1, p2, p3, p4)

# Solution exacte

I_exact = solution_analytique(a, b, p1, p2, p3, p4)

print("=" * 60)
print("  Mesure de performance – MGA802 Mini-Projet B")
print("=" * 60)
print(f"Intervalle : [{a}, {b}]  |  n = {N}  |  répétitions timeit = {REPETITIONS}")
print(f"Intégrale exacte : {I_exact:.6f}")
print()

# 1. perf_counter (une seule exécution)

print("─" * 60)
print("1. perf_counter (une seule exécution)")
print("─" * 60)

methodes = [
    ("Rectangles Python", rectangles_python),
    ("Rectangles NumPy ",  rectangles_numpy),
    ("Trapèzes    Python", integration_trapezes_python),
    ("Trapèzes    NumPy ", integration_trapezes),
    ("Simpson     Python", simpson_python),
    ("Simpson     NumPy ", simpson_numpy),
]

for nom, fn in methodes:
    tic = perf_counter()
    resultat = fn(*PARAMETRES)
    toc = perf_counter()
    erreur = calculer_erreur(resultat, I_exact)
    print(f"{nom} : {toc - tic:.6f} [s]  |  erreur = {erreur:.2e}")
print()

# 2. timeit (N répétitions)

print("─" * 60)
print(f"2. timeit ({REPETITIONS} répétitions)")
print("─" * 60)

appels = [
    ("Rectangles Python", "rectangles_python(*PARAMETRES)"),
    ("Rectangles NumPy ", "rectangles_numpy(*PARAMETRES)"),
    ("Trapèzes    Python", "integration_trapezes_python(*PARAMETRES)"),
    ("Trapèzes    NumPy ", "integration_trapezes(*PARAMETRES)"),
    ("Simpson     Python", "simpson_python(*PARAMETRES)"),
    ("Simpson     NumPy ", "simpson_numpy(*PARAMETRES)"),
]

for nom, stmt in appels:
    total = timeit(stmt, globals=globals(), number=REPETITIONS)
    print(f"{nom} : total = {total:.4f} [s]  |  moyenne = {total / REPETITIONS:.6f} [s]")
