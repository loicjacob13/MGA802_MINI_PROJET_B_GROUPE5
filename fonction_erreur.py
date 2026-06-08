
def calculer_erreur(valeur_numerique,valeur_exacte):
    #valeur numérique sera le return des 3 différents modules correspondant aux trois différentes méthodes
    #valeur exacte sera la valeur théorique exacte issu du module solution analytique.py

    difference=valeur_numerique-valeur_exacte

    erreur_absolue=abs(difference) #on veut une valeur absolue pour que l'erreur soit tout le temps positif
    return erreur_absolue


