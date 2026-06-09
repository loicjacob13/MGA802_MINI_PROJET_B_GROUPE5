"""
MGA802 - Mini-Projet B
Script de perf_counter & time_it
Mesure les temps d'exécution des méthodes d'intégration numérique
"""

from time import perf_counter
from timeit import timeit
from fonction_erreur import calculer_erreur

def benchmark_perf_counter(methodes, parametres, valeur_exacte):
    '''mesure le temps d'une seule exécution pour chaque méthode avec perf_counter'''
    print("\n─ perf_counter (une seule exécution) ─\n")
    for nom, fn in methodes: # on itère sur chaque (nom, fonction) de la liste
        tic = perf_counter() # on démarre le chrono
        fn(*parametres) #on appelle la fonction avec les paramètres
        toc = perf_counter() # on arrête le chrono
        erreur = calculer_erreur(fn(*parametres), valeur_exacte) # erreur par rapport à la solution exacte
        print(f"  {nom} : {toc - tic:.6f} [s]  |  erreur = {erreur:.2e}")

def benchmark_timeit(methodes, parametres, repetitions):
    '''mesure le temps moyen sur plusieurs répétitions avec timeit, plus fiable que perf_counter'''
    print(f"\n─ timeit ({repetitions} répétitions) ─\n")
    for nom, fn in methodes:
        # lambda fn=fn capture la valeur courante de fn pour éviter le bug de closure
        total = timeit(lambda fn=fn: fn(*parametres), number=repetitions)
        print(f"  {nom} : total = {total:.4f} [s]  |  moyenne = {total / repetitions:.6f} [s]")