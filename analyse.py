from fonction_erreur import calculer_erreur
import matplotlib.pyplot as plt

def convergence(fonction_integration, a, b, liste_n, p1, p2, p3, p4, valeur_exacte): #
    #ici fonction intégration servira à appeler chaque méthode différente
    #calcule l'erreur d'une méthode d'intégration pour plusieurs valeurs n
    #liste_n contiendra les différentes valeurs de segments à tester
    liste_erreurs = []  # on stockera ici l'erreur obtenue pour chaque n

    # On parcourt chaque nombre de segments demande
    for n in liste_n:
        # On calcule l'aire approximée avec la méthode fournie pour ce n
        valeur_numerique = fonction_integration(a, b, n, p1, p2, p3, p4)

        # On calcule l'erreur par rapport a la valeur exacte
        erreur = calculer_erreur(valeur_numerique, valeur_exacte)

        # On ajoute cette erreur a la liste des resultats
        liste_erreurs.append(erreur)

    return liste_erreurs

def generer_liste_n(n_min=10,n_max=100000,facteur=2):
    #génère liste de nombre de segments
    liste_n = []  # liste des nombres de segments a tester
    n = n_min  # on commence au minimum

    # Tant qu'on n'a pas dépasse le maximum, on ajoute n et on le multiplie
    while n <= n_max:
        liste_n.append(int(n))  # int() au cas ou le facteur est un nombre a virgule
        n = n * facteur  # on passe a la valeur suivante (plus grande)

    return liste_n

def tracer_convergence(liste_n, dictionnaire_erreurs, nom_fichier="convergence.png"):
    #on va utiliser le dictionnaire des erreurs : {nom_de_la_methode : liste_des_erreurs}
    #échelle log-log utilisée
    #trace graphique de convergence: erreur en fonction du nombre de segments
    fig, ax = plt.subplots(figsize=(8, 6)) #création figure et des axes

    #pour chaque méthode qui sera dans le dicxtionnaire, on va tracer la courbe
    for nom_methode in dictionnaire_erreurs:
        liste_erreurs = dictionnaire_erreurs[nom_methode]
        ax.loglog(liste_n, liste_erreurs,marker='o', label=nom_methode) #axe log log pour les axes x et y

        #création titre, légende et grille
        ax.set_xlabel("nombre de segments n")
        ax.set_ylabel("erreur (en valeur absolue)")
        ax.set_title("convergence des methodes d'integration")
        ax.legend()
        ax.grid(True, which="both")  # which="both" : grille sur grandes (puissances de 10) et petites graduations (valeurs intermédiaires)

        # sauvegarde dans un fichier (l'extension determine le format) et l'affichage
        fig.savefig(nom_fichier)
        plt.show()
