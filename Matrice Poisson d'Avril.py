# from math import *
from random import *
from time import *
# from pprint import pprint


def mystere_ligne(carre):
    magic = False
    s = 0
    for ligne in range(len(carre)):
        s = 0
        for colonne in range(len(carre[ligne])):
            s += carre[ligne][colonne]
        print(f"somme = {s}")

    if s == 15:
        magic = True

    return magic


def mystere_diagonale1(carre):
    magic = False
    s = 0
    for ligne in range(len(carre)):
        s += carre[ligne][ligne]
    print(f"somme = {s}")

    if s == 15:
        magic = True

    return magic


def mystere_diagonale2(carre):
    magic = False
    s = 0
    for ligne in range(len(carre)):
        s += carre[ligne][(len(carre) - 1) - ligne]
    print(f"somme = {s}")

    if s == 15:
        magic = True

    return magic


def mystere_colonne(carre):
    magic = False
    s= 0
    for colonne in range(len(carre)):
        s = 0
        for ligne in range(len(carre[colonne])):
            s += carre[ligne][colonne]
        print(f"somme = {s}")

    if s == 15:
        magic = True

    return magic


Carre1 = [[8, 3, 1], [1, 5, 9], [2, 7, 2]]
Carre2 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
Carre = choice([Carre1, Carre2])
Magic1 = mystere_ligne(Carre)
Magic2 = mystere_diagonale1(Carre)
Magic3 = mystere_diagonale2(Carre)
Magic4 = mystere_colonne(Carre)

if Magic1 and Magic2 and Magic3 and Magic4:
    print(f"Votre carré {Carre} est magique !")
else:
    print(f"Votre carré {Carre} n'est pas magique !")
