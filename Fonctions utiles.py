from math import *
from random import *
# from time import *


def get_hypothenuse(cote1, cote2):                                              # Get the hypothenuse of a triangle
    return sqrt(cote1 ** 2 + cote2 ** 2)


def fonction_perso(nb):                                                         # Random 2nd degree function
    return nb ** 2 + nb * 3 + 2


def get_average(notes):                                                         # Get the average of several numbers
    somme = 0
    for note in notes:
        somme += note
    return somme / len(notes)


def get_ppcm(*args):                                                            # Get smaller coefficient ?
    print(f"Arguments entrés : {args}")
    L = list(args)
    if len(L) == 2:
        return get_sum_common_prime_factor(L[0], L[1])
    else:
        n = len(L)
        i = 0
        A = []
        while i <= n - 2:
            A.append(get_sum_common_prime_factor(L[i], L[i + 1]))
            i += 2

        if n % 2 != 0:
            A.append(L[n - 1])

        return get_sum_common_prime_factor(*A)


def get_sum_common_prime_factor(a, b):
    Da = get_prime_factor(a)
    Db = get_prime_factor(b)
    p = 1
    for facteur, exposant in Da.items():
        if facteur in Db:
            expo = max(exposant, Db[facteur])
        else:
            expo = exposant

        p *= facteur ** expo

    for facteur, exposant in Db.items():
        if facteur not in Da:
            p *= facteur ** exposant

    return p


def get_prime_factor(n):
    print(f"Facteurs premiers de {n} : ", end="")
    L = dict()
    k = 2
    while n != 1:
        xp = 0
        while n % k == 0:
            n //= k
            xp += 1
        if xp != 0:
            L[k] = xp
        k += 1
    for _ in L:
        print(_, end=" ")
    print("")

    return L


# -------------------------------------------------------------------------------
def generate_nb_in_ascending(end: int, nb: int):
    result = []
    liste = [_ for _ in range(end)]

    for i in range(nb):
        choix = choice(liste)
        result.append(choix)
        liste.remove(choix)

    result.sort()

    for r in result:
        print(r, end=" ")

    return result


if __name__ == "__main__":
    print(get_hypothenuse(3, 1) ** 2)
    # print(fonction_perso(7))
    # print(get_average([8/20, 12.5/20, 15/20, 18/20, 17.5/20, 14/20, 6/20, 9.5/20, 19.5/20, 7/20, 16/20, 13/20]) * 20)
    # generate_nb_in_ascending(37, 6)
    # print(f"Résultat : {get_ppcm(26, 36, 90)}")

quit()
