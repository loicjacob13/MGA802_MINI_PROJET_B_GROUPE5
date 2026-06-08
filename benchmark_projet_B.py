"""
MGA802 - Mini-Projet B
Script de perf_counter & time_it
Mesure les temps d'exécution des méthodes d'intégration numérique
"""

from time import perf_counter
from timeit import timeit
from fonction_erreur import calculer_erreur

def benchmark_perf_counter(methodes, parametres, valeur_exacte):
    print("\n─ perf_counter (une seule exécution) ─")
    for nom, fn in methodes:
        tic = perf_counter()
        fn(*parametres)
        toc = perf_counter()
        erreur = calculer_erreur(fn(*parametres), valeur_exacte)
        print(f"  {nom} : {toc - tic:.6f} [s]  |  erreur = {erreur:.2e}")

def benchmark_timeit(methodes, parametres, repetitions):
    print(f"\n─ timeit ({repetitions} répétitions) ─")
    for nom, fn in methodes:
        total = timeit(lambda fn=fn: fn(*parametres), number=repetitions)
        print(f"  {nom} : total = {total:.4f} [s]  |  moyenne = {total / repetitions:.6f} [s]")