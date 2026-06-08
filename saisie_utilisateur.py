def demander_float(message):
    #demande un nombre réel à l'utilisateur et le renvoie
    #tant que la saisie n'est poas un nombre valide, on va redemander à l'user
    #permet de ne pas renvoyer une erreur
    while True:
        try:
            valeur = float(input(message))  # echoue si ce n'est pas un nombre
            return valeur
        except ValueError: # il n'y a pas de return donc on va redema,der à l'user de saisir un autre terme
            print("Erreur : saisissez un nombre valide (ex : 2 ou 3.5).")


def demander_entier_positif(message):
    #vérifie si le nombre de segments est positif différent de 0 et entier
    while True:
        try:
            valeur = int(input(message))  # echoue si ce n'est pas un entier
        except ValueError:
            print("Erreur : saisissez un nombre entier (ex : 10).")
            continue  # on redemande
            #le continue est indispensable sinon on testerait si l'input est bien positif alors que ça pourrait ne même pas être un float
        if valeur <= 0:
            print("Erreur : le nombre de segments doit etre strictement positif.")
            continue  # on redemande
        return valeur


def demander_bornes():
    #va demander les 2 bornes d'intégration a et b
    #vérifie si a est bien différent de b sinon pas de sens
    #rennvoie le couple (a,b)
    while True:
        a=demander_float("borne inférieure a : ")
        b = demander_float("borne supérieure b : ")
        if b<=a :
            print("Erreur : la borne b doit être strictement supérieure à la borne a , recommencez ")
            continue #on redemande donc les 2 bornes
        return a, b

def demander_coefficients():
    #va demander les 4 coefficients à l'user
    #renvoie le quadruplet (p1,p2,p3,p4)
    print("Saisie des coefficients du polynome f(x) = p1 + p2*x + p3*x^2 + p4*x^3")
    p1 = demander_float("Coefficient p1 (terme constant) : ")
    p2 = demander_float("Coefficient p2 (terme en x) : ")
    p3 = demander_float("Coefficient p3 (terme en x^2) : ")
    p4 = demander_float("Coefficient p4 (terme en x^3) : ")
    return p1, p2, p3, p4