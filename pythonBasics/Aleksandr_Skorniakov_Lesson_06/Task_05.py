from json import dump
from itertools import zip_longest
from sys import argv
import os


def users_hobbies(users_f, n_users_f, hobbies_f, n_hobbies_f, users_hobbies_f, n_users_hobbies_f):
    os.rename(users_f, n_users_f)
    os.rename(hobbies_f, n_hobbies_f)
    os.rename(users_hobbies_f, n_users_hobbies_f)

    with open(n_users_f, 'r', encoding='utf-8') as users:
        with open(n_hobbies_f, 'r', encoding='utf-8') as hobbies:

            users_hobby = zip_longest((user for user in users), hobbies, fillvalue='None')
            form = {info[0].strip().replace(',', ' '): (info[1]).strip().replace(',', ', ') for info in users_hobby}

            with open(n_users_hobbies_f, 'w', encoding='utf-8') as f:
                if 'None' not in form:
                    dump(form, f, indent=4, ensure_ascii=False)
                    f.write('\n')
                else:
                    exit(1)


if __name__ == '__main__':
    users_hobbies(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6])
