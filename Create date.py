# from math import *
from random import *
# from time import *
from datetime import *
# from pprint import pprint


def create_date():                                                              # Create a random date : not perfect
    day = str(randint(1, 31))
    if len(day) < 2:
        day = "0" + day
    month = str(randint(1, 12))
    if len(month) < 2:
        month = "0" + month
    year = str(randint(1900, date.today().year))

    return f"{day}/{month}/{year}"


def get_date_infos(date_format_jj_mm_aaaa=None, date_format_aaaa_mm_jj=None):   # return infos based on date format
    if date_format_jj_mm_aaaa:
        day = str(date_format_jj_mm_aaaa)[0:2]
        month = str(date_format_jj_mm_aaaa)[3:5]
        year = str(date_format_jj_mm_aaaa)[6:10]
    elif date_format_aaaa_mm_jj:
        day = str(date_format_aaaa_mm_jj)[8:10]
        month = str(date_format_aaaa_mm_jj)[5:7]
        year = str(date_format_aaaa_mm_jj)[0:4]
    else:
        date_format = datetime.date(datetime.today())
        day = str(date_format)[8:10]
        month = str(date_format)[5:7]
        year = str(date_format)[0:4]

    return day, month, year


def is_futur(date_tested, date_referenced):                                     # Check the earlier date
    jour_t, mois_t, annee_t = get_date_infos(date_tested)
    jour_ref, mois_ref, annee_ref = get_date_infos(date_referenced)

    if annee_ref < annee_t:
        return 1
    elif annee_ref > annee_t:
        return -1
    else:
        if mois_ref < mois_t:
            return 1
        elif mois_ref > mois_t:
            return -1
        else:
            if jour_ref < jour_t:
                return 1
            elif jour_ref > jour_t:
                return -1
            else:
                return 0


def get_dates_infos_futures(set_date_t=False, set_date_ref=False):
    date_t = input("Date testée : (dd/mm/aaaa) ").replace(" ", "") if set_date_t else create_date()
    date_ref = input("Date de référence : (dd/mm/aaaa) ").replace(" ", "") if set_date_ref else create_date()
    print(f"Date testée : {date_t}")
    print(f"Date de référence : {date_ref}")
    if is_futur(date_t, date_ref) > 0:
        print(f"Date la plus veille : {date_ref}")
    elif is_futur(date_t, date_ref) < 0:
        print(f"Date la plus veille : {date_t}")
    else:
        print(f"Les deux dates sont la même !")


get_dates_infos_futures(False, True)

quit()
