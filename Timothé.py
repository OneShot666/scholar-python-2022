from math import *
from random import *
from time import *
from copy import *

"""   Creation d'idée en cours   """


def Conway(n):
    suite = "1"
    Suites = [suite]

    for i in range(n):                                      # N° de la ligne
        print(f"{suite}")
        sleep(0.2)

        minisuite = suite[0]
        for j in range(1, len(suite)):                      # Position dans la suite
            if suite[j - 1] == suite[j]:
                minisuite += suite[j - 1]
                print(f"Minisuite : {minisuite}")
            else:
                minisuite = suite[j]

        print(f"Groupe : {len(minisuite)}")
        suite += str(len(minisuite))

        if suite[-1] != "1":
            suite += "1"

        Suites.append(suite)

    return Suites


graines = Conway(5)
for el in graines:
    exit()
    print(f"{el}")
