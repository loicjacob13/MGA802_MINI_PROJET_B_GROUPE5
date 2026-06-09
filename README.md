# Mini-Projet B — Intégration numérique (MGA802)

Auteurs: Loïc Jacob (JACL93280301) ; Fabien Koch (KOCF83320301) ; Guillaume Pissang (PISG89300201)
## 1. À quoi sert ce programme

Ce programme calcule l'aire sous la courbe d'une fonction polynomiale du 3e ordre :

f(x) = p1 + p2*x + p3*x^2 + p4*x^3

sur un intervalle [a, b]. Calculer cette aire, c'est ce qu'on appelle intégrer la fonction.

Le but du projet est de comparer plusieurs méthodes pour calculer cette aire, et de voir laquelle est la plus précise et la plus rapide. On compare :

- Des méthodes écrites en Python de base, avec des boucles, simples mais lentes.
- Les mêmes méthodes écrites avec NumPy, une bibliothèque de calcul rapide.
- Les méthodes déjà toutes prêtes de SciPy, une bibliothèque scientifique.

Trois méthodes mathématiques sont utilisées : rectangles, trapèzes et Simpson. Ce sont trois façons différentes d'approcher l'aire en découpant l'intervalle en petits morceaux appelés segments. Plus on utilise de segments (le nombre n), plus le résultat est précis.

## 2. Ce dont vous avez besoin

### Version de Python

Python 3, testé avec Python 3.11.

### Bibliothèques à installer

Le programme utilise des bibliothèques externes. Il faut les installer avant de lancer le programme, sinon il ne démarrera pas. Ouvrez un terminal et tapez :

pip install numpy matplotlib scipy

Rôle de chaque bibliothèque :

- **numpy** : calcul rapide sur des tableaux de nombres, pour les versions NumPy des méthodes.
- **matplotlib** : sert à dessiner les graphiques.
- **scipy** : contient les méthodes d'intégration déjà programmées, trapèzes et Simpson.

Les modules time et timeit, utilisés pour mesurer le temps, sont déjà inclus dans Python. Il n'y a rien à installer pour eux.

## 3. Comment lancer le programme

Lancez le fichier **main.py**. C'est le seul fichier à exécuter : il s'occupe d'appeler automatiquement tous les autres.

Le programme va vous poser des questions une par une dans la console :

- Les 4 coefficients du polynôme : p1, p2, p3, p4.
- Les bornes de l'intervalle : a et b. La borne b doit être plus grande que a.
- Le nombre de segments n, un nombre entier positif.
- Le nombre de répétitions pour la mesure de temps, le benchmark.

Si vous tapez quelque chose d'incorrect, comme une lettre au lieu d'un nombre, le programme ne plante pas : il vous le signale et vous redemande la valeur.

### Important : fermer les graphiques pour continuer

Pendant son exécution, le programme affiche des graphiques dans une fenêtre séparée.

**Tant que cette fenêtre est ouverte, le programme est en pause et n'avance pas.** Vous devez fermer la fenêtre du graphique pour que le programme reprenne et passe à la suite.

Il y a deux graphiques au total, qui s'affichent à des moments différents :

- Le graphique de convergence, l'erreur en fonction de n.
- Le graphique du temps de calcul, le temps en fonction de n.

À chaque fois, pensez à fermer la fenêtre pour accéder à la suite du programme.

### Conseil sur le nombre de répétitions

Pour la mesure de temps, un grand nombre de répétitions, par exemple 12000, rend le programme très lent à finir. Pour des tests rapides, entrez plutôt une petite valeur comme 100. Le résultat reste fiable.

## 4. Ce que le programme affiche

Le programme produit, dans l'ordre :

- Le graphique de convergence : montre comment l'erreur de chaque méthode diminue quand on augmente le nombre de segments.
- Un tableau de résultats dans la console : pour le n que vous avez choisi, l'aire calculée et l'erreur de chaque méthode.
- Un benchmark dans la console : le temps de calcul de chaque méthode.
- Le graphique du temps de calcul : montre que les versions NumPy sont plus rapides que les versions Python de base quand n devient grand.

Les deux graphiques sont aussi enregistrés en fichiers images, convergence.png et temps.png, dans le dossier du projet. C'est normal qu'ils restent après l'arrêt du programme : ils servent à être réutilisés, par exemple dans le rapport.

## 5. Organisation des fichiers

Le projet est découpé en plusieurs fichiers, chacun ayant une responsabilité précise. Le fichier main.py est le chef d'orchestre : il appelle tous les autres.

- **main.py** : programme principal. Pose les questions, appelle toutes les méthodes, affiche les résultats et les graphiques. C'est le fichier à lancer.
- **saisie_utilisateur.py** : pose les questions à l'utilisateur et vérifie que les réponses sont valides, un nombre, un entier positif, b plus grand que a. Empêche le programme de planter.
- **solution_analytique.py** : calcule la valeur exacte de l'aire par les mathématiques. Sert de référence pour mesurer l'erreur des autres méthodes.
- **rectangles.py** : méthode des rectangles, en Python de base et en NumPy.
- **trapezes.py** : méthode des trapèzes, en Python de base et en NumPy.
- **simpson.py** : méthode de Simpson, en Python de base et en NumPy.
- **methodes_preprogrammees.py** : méthodes des trapèzes et de Simpson déjà toutes prêtes dans SciPy.
- **fonction_erreur.py** : calcule l'erreur, la différence en valeur absolue entre une aire calculée et l'aire exacte.
- **analyse.py** : étudie la convergence, l'erreur selon n, et le temps de calcul, le temps selon n, et dessine les deux graphiques.
- **benchmark_projet_B.py** : mesure et affiche le temps de calcul de chaque méthode dans la console.

## 6. Comment le code fonctionne, étape par étape

Pour quelqu'un qui débute, voici la logique générale, sans entrer dans les maths :

- **On demande les paramètres.** L'utilisateur entre la fonction, ses coefficients, l'intervalle et le nombre de segments.
- **On calcule la bonne réponse.** Le module solution_analytique.py donne l'aire exacte. C'est la référence : toutes les autres méthodes seront comparées à elle.
- **On calcule l'aire avec chaque méthode.** Chaque méthode découpe l'intervalle en n morceaux et additionne les petites aires. Chaque méthode existe en deux versions : une lente en Python de base avec une boucle, et une rapide avec NumPy.
- **On mesure l'erreur.** Pour chaque méthode, on compare son résultat à l'aire exacte. Plus l'écart est petit, meilleure est la méthode.
- **On étudie la convergence.** On refait le calcul pour des n de plus en plus grands, 10, 20, 40, et ainsi de suite, et on regarde si l'erreur diminue. C'est le premier graphique.
- **On mesure le temps.** On chronomètre chaque méthode. C'est le benchmark affiché dans la console et le deuxième graphique. On voit alors que NumPy est beaucoup plus rapide que Python de base quand le nombre de segments est élevé.

## 7. Remarque sur la méthode de Simpson

La méthode de Simpson est exacte pour les polynômes de degré inférieur ou égal à 3. Comme la fonction étudiée est exactement de degré 3, Simpson donne une erreur quasiment nulle, de l'ordre de 10^-14, ce qui correspond à la précision maximale de l'ordinateur. C'est normal et attendu.
