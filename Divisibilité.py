# from math import *
from random import *
from time import *
# from pprint import pprint


def is_divisible_len_3(number: str):
    if int(number[0]) + int(number[2]) == int(number[1]):
        return True
    else:
        return False


def is_divisible_len_unknown(number: str):
    sum_pair = 0
    sum_impair = 0
    for i in range(len(number)):
        if i % 2 == 0:
            sum_pair += int(number[i])
        else:
            sum_impair += int(number[i])

    if sum_pair == sum_impair:
        return True
    else:
        return False


def inverse_string(string: str):
    return reversed(string)


def genere(number: int):
    if abs(number) % 2 == 0 or is_divisible_len_unknown(str(number)):
        resultat = ""
        for i in range(number):
            resultat += randint(0, 9)
        resultat += reversed(resultat)
        return resultat
    else:
        return None


quit()
