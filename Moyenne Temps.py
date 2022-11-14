from math import *
from random import *
from time import *


def time_in_second(temps_hh_mm_ss: str):
    return int(temps_hh_mm_ss[:2]) * 3600 + int(temps_hh_mm_ss[3:5]) * 60 + int(temps_hh_mm_ss[6:])


print(f"{time_in_second('00.14.30')} seconds")
