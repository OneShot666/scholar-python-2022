# import math
# import random
# import time


def Exercice10(taille: int = None, tronc: int = None, branche: int = None):
    if taille is None:
        taille = int(input("Entrer la taille du sapin : "))
    if tronc is None:
        tronc = int(input("Entrer la taille du tronc du sapin : "))
    if branche is None:
        branche = int(input("Entrer la taille des branches du sapin : "))
    bosquet = int(taille / branche)

    for i in range(bosquet):
        for j in range(branche):
            ligne = ""
            if j < branche - 1:
                ligne += " " * (branche - (j + 1))
                ligne += "/"
                ligne += " " * j * 2
            else:
                ligne += "/"
                ligne += "_" * (branche - 1) * 2
            ligne += "\\"
            print(ligne)

    for j in range(tronc):
        ligne = " " * int(branche - 2)
        ligne += "|  |"
        print(ligne)


if __name__ == "__main__":
    Exercice10(24, 5, 8)

quit()
