from fonction_erreur import calculer_erreur


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

