
import numpy as np
import random
from random import randint
import string


int_list = [83, 93, 46, 16, 34, 18, 17, 31, 43, 34, 99, 46, 32, 8, 54, 96, 23, 80, 49, 34, 19, 32, 35, 48, 80, 33, 9, 31, 84, 22, 2, 87, 50, 79, 31, 53, 50, 9, 27, 72, 97, 89, 57, 40, 34, 33, 78, 78, 27, 30, 87, 37, 33, 51, 93, 80, 93, 71, 75, 74, 83, 38, 4, 82, 28, 75, 88, 95, 18, 0, 79, 37, 0, 36, 75, 27, 16, 79, 10, 8, 20, 50, 77, 23, 55, 2, 2, 21, 49, 51, 85, 36, 95, 68, 57, 22, 15, 53, 7, 89]

string_to_generate_human_ID = string.ascii_uppercase + string.ascii_lowercase + string.digits

string = ["komp", "beka", "ogorek", "dom", "auto", "wodka", "muzyka", "kraft_beer", "praca", "python", "share_point"]
bool = [True, False]
name = ["Janusz", "Grazyna", "Zuza", "Marian", "Bolek", "Zbigniew"]
surname = ["Gaca", "Belkot", "Babelek", "Janik", "Drugi", "Pech"]
fullname = ["Janusz Gaca", "Grazyna Belkot", "Zuza Babelek", "Marian Janik", "Bolek Drugi", "Zbigniew Pech"]
email = ["janusz.gaca@amorki.pl", "grazyna_belkot@wp.pl", "zuza.babelek@malpa.eu", "marian_janik@onet.pl", "bolek.drugi@o2.pl", "zbigniew_pech@lublin.eu"]
age = [50, 31, 22, 15, 18, 35, 44, 77, 73, 78, 13, 65, 23, 34, 54]
weight = [90, 55, 60, 64, 85, 53, 66, 44, 91, 68]
height = [177, 160, 155, 180, 183, 158, 162, 166]

_range = 3
error_message = np.array('wrong type / _range has to be integer')
lenght = 5

# print(int)
# print(scope)
# print(string)
# print(bool)
# print(name)
# print(surname)
# print(fullname)
# print(email)

def gen_hash(lenght):

    human_ID = ''.join(random.choice(string_to_generate_human_ID) for _ in range(lenght))

    return human_ID


def gen_n_int_list(_range):

    if type(_range) == int:

        new_int_list = [random.choice(int_list) for number in range(_range)]

        new_int_np_list = np.array(new_int_list)

        return new_int_np_list

    else:

        return error_message


def gen_n_string_list(_range):

    if type(_range) == int:

        new_string_list = [random.choice(string) for number in range(_range)]

        new_string_np_list = np.array(new_string_list)

        return new_string_np_list

    else:

        return error_message


def gen_n_bool_list(_range):

    if type(_range) == int:

        new_bool_list = [random.choice(bool) for number in range(_range)]

        new_bool_np_list = np.array(new_bool_list)

        return new_bool_np_list

    else:

        return error_message


def gen_n_name_list(_range):

    if type(_range) == int:

        new_name_list = [random.choice(name) for number in range(_range)]

        new_name_np_list = np.array(new_name_list)

        return new_name_np_list

    else:

        return error_message


def gen_n_surname_list(_range):

    if type(_range) == int:

        new_surname_list = [random.choice(surname) for number in range(_range)]

        new_surname_np_list = np.array(new_surname_list)

        return new_surname_np_list

    else:

        return error_message


def gen_n_fullname_list(_range):

    if type(_range) == int:

        new_fullname_list = [random.choice(fullname) for number in range(_range)]

        new_fullname_np_list = np.array(new_fullname_list)

        return new_fullname_np_list

    else:

        return error_message


def gen_n_email_list(_range):

    if type(_range) == int:

        new_email_list = [random.choice(email) for number in range(_range)]

        new_email_np_list = np.array(new_email_list)

        return new_email_np_list

    else:

        return error_message


def gen_age_list(_range):

    if type(_range) == int:

        new_age_list = [random.choice(age) for number in range(_range)]

        new_age_np_list = np.array(new_age_list)

        return new_age_np_list

    else:

        return error_message


def gen_weight_list(_range):

    if type(_range) == int:

        new_weight_list = [random.choice(weight) for number in range(_range)]

        new_weight_np_list = np.array(new_weight_list)

        return new_weight_np_list

    else:

        return error_message


def gen_height_list(_range):

    if type(_range) == int:

        new_height_list = [random.choice(height) for number in range(_range)]

        new_height_np_list = np.array(new_height_list)

        return new_height_np_list

    else:

        return error_message
