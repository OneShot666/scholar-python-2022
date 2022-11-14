# from math import *
from random import *
# from time import *
from pprint import pprint

nb = int(input(f"Combien de matrices : "))

for n in range(nb):
    cote = int(input(f"Insérer une taille : "))
    alea = input(f"Matrice aléatoire (y/n) : ")
    algo = ""
    hasard = False
    carre = False
    perfect = False

    if alea == "y":
        hasard = True
        carre = input(f"Matrice au carré (y/n) : ")
        if carre == "y":
            carre = True
            perfect = input(f"Matrice parfaite (y/n) : ")
            if perfect == "y":
                perfect = True
    else:
        algo = input(f"Insérer un programme (i, j) : ")
        algo.lower()

    Matrice = [[_ for _ in range(cote)] for _ in range(cote)]
    if carre:
        Choix = [_ for _ in range(cote ** 2)]
    else:
        Choix = [_ for _ in range(cote)]

    for i in range(cote):
        for j in range(cote):
            valeur = 0
            if hasard:
                valeur = choice(Choix)
                if perfect:
                    Choix.remove(valeur)
            else:
                if algo == "i":
                    valeur = i
                elif algo == "j":
                    valeur = j
                elif algo == "i + j":
                    valeur = i + j
                elif algo == "i - j":
                    valeur = i - j
                elif algo == "i x j":
                    valeur = i * j
                elif algo == "i / j":
                    valeur = i / j
                elif algo == "i ^ j":
                    valeur = i ** j
                else:
                    print(f"Le programme '{algo}' n'a pas été reconnu !")
                    cote = 0
                    break

            Matrice[i][j] = valeur

    pprint(Matrice)
