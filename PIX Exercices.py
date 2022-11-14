# from math import *
# from random import *
from time import *
from copy import *


"""   Exercices Programmer : Toc toc   """
"""
toc toc tic toc toc toc toc tic toc tic tic toc tic toc tic tic tic toc toc toc

Code = {key: value for d in ({" ": 0}, {chr(_ + 64): _ for _ in range(1, 27)}) for key, value in d.items()}
print(Code)


def TicToc_to_Binaire(tictoc=None):
    if tictoc is None:
        tictoc = input("Entrer les sons tic & toc : ")
    tictoc.lower()
    tictoc = tictoc.replace(" ", "")

    for i in range(0, len(tictoc), 1):
        mot = tictoc[i: i + 3]
        if mot == "tic":
            mot = 1
        elif mot == "toc":
            mot = 0
        else:
            mot = ""
        tictoc = tictoc[0: i] + str(mot) + tictoc[i + 3: len(tictoc)]

    return tictoc


def Binaire_to_Decimal(binaire: int = None):
    if binaire is None:
        binaire = input("Veuillez saisir un nombre en binaire : ")
    if type(binaire) == str:
        binaire = binaire.replace(" ", "")
    else:
        binaire = str(binaire)
    decimal = int(binaire, 2)
    return int(decimal)


def Decodage():
    code = input("Entrer le code : ")
    code = TicToc_to_Binaire(code)
    print(f"Code tictoc : {code}\n")
    sleep(1)
    Messages = []

    for i in range(1, len(code)):
        message = ""

        for chiffre in range(0, len(code), i):                              # Essaie par différentes tranches
            element = int(code[chiffre: chiffre + i])
            element = Binaire_to_Decimal(element)

            if element in Code.values():
                for key, value in Code.items():
                    if element == value:
                        message += str(key)
                        break

        if message != "":
            Messages.append(message)

    return Messages


Decodes = Decodage()
for nb in range(len(Decodes)):
    print(f"Code n°{nb + 1} : ", '\t' * 1, f"'{Decodes[nb]}'")
    sleep(0.2)
"""

"""   Exercices Programmer : Codage de Huffman (gain de bit)   """
Code = {" ": 5, "D": 4, "M": 4, "N": 6, "O": 6, "T": 5, "U": 5}


def get_taux_impression(phrase: str = None):
    if phrase is None:
        phrase = input("Entrer une phrase : ")
    phrase.upper()
    lgr = len(phrase)
    bit_size = lgr * 8
    taux_size = deepcopy(bit_size)

    for lettre in phrase:
        for nom, valeur in Code.items():
            if lettre == nom:
                taux_size -= valeur

    compression = taux_size / bit_size * 100

    return compression


taux = get_taux_impression()
print(f"Taux de compression : {taux}%")
