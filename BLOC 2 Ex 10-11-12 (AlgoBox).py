# from math import *
from random import *
# from time import *
from copy import *

"""   Exercice 10   """                                    # Problèmes : - ex12, ajout last él av 1er él
Tableau = []                                               # - taille trop grand ap ex 10
newTableau = []                                            # - ex 11-12, last él en double
taille = 10
drapeau = False

for i in range(taille):
    valeur = randint(0, 100)
    Tableau.append(valeur)
    print(Tableau[i], end=" ")
print("<- Tableau non trié")

for i in range(taille):
    for y in range(taille - 1):
        if Tableau[y] > Tableau[y + 1]:
            ui = deepcopy(Tableau[y])
            Tableau[y] = Tableau[y + 1]
            Tableau[y + 1] = ui

for i in range(taille):
    print(Tableau[i], end=" ")
print("<- Tableau trié")

"""   Exercice 11   """
nb = int(input("Entrer le nombre à ajouter : "))

for i in range(taille):
    if Tableau[i] < nb or drapeau:
        if not drapeau:
            newTableau.append(Tableau[i])
        else:
            newTableau.append(Tableau[i - 1])
    else:
        newTableau.append(nb)
        drapeau = True

for i in range(len(newTableau) - 1):
    print(newTableau[i], end=" ")
print("<- Tableau trié (avec ajout)")

"""   Exercice 12   """
drapeau = 0
nb = int(input("Entrer le nombre à retirer : "))

for i in range(taille):
    y = 0
    if newTableau[i] == nb:
        drapeau += 1
        for y in range(i, len(newTableau) - 1):
            newTableau[y] = newTableau[y + 1]
            i = i - 1
    else:
        newTableau[y] = newTableau[i]

for i in range(taille - drapeau):
    print(newTableau[i], end=" ")
print("<- Tableau trié (avec suppression)")
