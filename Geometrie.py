from math import *
from random import *
# from time import *


# Ajouter calcul avec angles
class Geometry:
    def __init__(self):
        __name__ = "Thalès"

    @staticmethod
    def getPerimetreCercle(rayon):
        return 2 * pi * rayon

    """ Marche avec tout les quadrilatères """
    @staticmethod
    def getPerimetreRectangle(longueur, largeur):
        return (longueur + largeur) * 2

    """ Marche avec tous les triangles """
    @staticmethod
    def getPerimetreTriangle(cote1, cote2, cote3):
        return cote1 + cote2 + cote3

    @staticmethod
    def getPerimetrePolygone(*args):
        return sum(args)

    @staticmethod
    def getAireCercle(rayon):
        return 4 * pi * rayon ** 2

    @staticmethod
    def getAireCylindre(rayon, hauteur):
        return 2 * pi * rayon * hauteur + 2 * pi * rayon ** 2

    @staticmethod
    def getAireOvale(rayon1, rayon2):
        return pi * rayon1 * rayon2

    """ Marche avec tout type de triangles """
    @staticmethod
    def getAireTriangle(base, hauteur):
        return base * hauteur / 2

    @staticmethod
    def getAireTrapeze(base1, base2, hauteur):
        return (base1 + base2) * hauteur / 2

    """ Marche aussi avec carré """
    @staticmethod
    def getAireRectangle(longueur, largeur):
        return longueur * largeur

    @staticmethod
    def getVolumeCone(rayon, hauteur):
        return 1 / 3 * pi * hauteur * rayon ** 2

    @staticmethod
    def getVolumeCylindre(rayon, hauteur):
        return hauteur * pi * rayon ** 2

    """ Marche aussi avec cube, prisme """
    @staticmethod
    def getVolumePave(longueur, largeur, hauteur):
        return longueur * largeur * hauteur

    @staticmethod
    def getVolumePyramide(longueur, largeur, hauteur):
        return 1 / 3 * longueur * largeur * hauteur

    @staticmethod
    def getVolumeSphere(rayon):
        return 4 / 3 * pi * rayon ** 3


if __name__ == "__main__":
    thales = Geometry()
    # print(f"Aire triangle : {thales.getAireTriangle(3.9, 8)} cm2")
    # print(f"Volume cône : {thales.getVolumeCone(2.3, 6)} cm3")
    print(f"Volume pavé : {thales.getVolumePave(256, 28.50, 52.60)} m3")
    # print(f"Volume cylindre : {thales.getVolumeCylindre(1.5, 600)} cm3")
    # print(f"Volume demi-sphère : {thales.getVolumeSphere(2.3) / 2} cm3")

quit()
