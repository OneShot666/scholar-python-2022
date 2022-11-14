# from math import *
from random import *
from time import *
# from pprint import pprint


def Creer_Carre(element=0, magic=False):
    while element <= 0:
        element = int(input("Entrer le nombre d'éléments par ligne et colonne : "))
    carre = [[0 for _ in range(element)] for _ in range(element)]

    perso = input(f"Entrer les valeurs manuellement ? (y/n) ")

    if perso != "y" or perso != "yes":
        repet = input(f"Faire un carré magique ? (y/n) ")

        if repet == "y" or repet == "yes":
            magic = True

    if perso == "y" or perso == "yes":
        for i in range(element):
            for j in range(element):
                valeur = int(input(f"Entrer une valeur pour la case[{i}][{j}] : "))
                carre[i][j] = valeur
    else:
        choix = [_ + 1 for _ in range(element ** 2)]
        for i in range(element):
            for j in range(element):
                valeur = choice(choix)
                if magic:
                    choix.remove(valeur)
                carre[i][j] = valeur
    print(f"")

    return carre


def Afficher_Carre(carre=None):
    if carre is None:
        carre = []
    print("Carré magique : ")
    sleep(0.5)

    for ligne in carre:
        for element in str(ligne):
            print(element, end="")
            sleep(0.2)
        print("")
    print("")


def Check_Magique(carre: list):                             # Doit vérifier si la somme est égale partout
    cote = len(carre)
    Lignes = []
    Colonnes = []
    magic = True

    for i in range(cote):
        for j in range(cote):
            if carre[i][j] not in Lignes:
                Lignes.append(carre[i][j])
            elif carre[j][i] not in Colonnes:
                Colonnes.append(carre[j][i])
            else:
                magic = False
                cote = 0
                break

    return magic


def get_luminescence(carre: list):                                     # Calcule moyenne valeurs dans Matrice
    somme = 0
    cote = len(carre) ** 2

    for ligne in carre:
        somme += sum(ligne)

    return somme / cote


square = Creer_Carre()
Afficher_Carre(square)
its_a_kind_of = Check_Magique(square)
if its_a_kind_of:
    message = f"Votre carré est magique ! "
else:
    message = f"Votre carré n'est pas magique... "
print(message)
lumin = get_luminescence(square)
print(f"Luminescence de votre Matrice : {lumin}")

# C01nB4se666
quit()
