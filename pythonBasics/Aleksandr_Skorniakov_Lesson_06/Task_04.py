from json import dump
from itertools import zip_longest


def users_hobbies():
    with open('users.csv', 'r', encoding='utf-8') as users:
        with open('hobbies.csv', 'r', encoding='utf-8') as hobbies:

            users_hobby = zip_longest((user for user in users), hobbies, fillvalue='None')
            form = {info[0].strip().replace(',', ' '): (info[1]).strip().replace(',', ', ') for info in users_hobby}

            with open('users_hobbies_04.txt', 'w', encoding='utf-8') as f:
                if 'None' not in form:
                    dump(form, f, indent=4, ensure_ascii=False)
                    f.write('\n')
                else:
                    exit(1)


if __name__ == '__main__':
    users_hobbies()
