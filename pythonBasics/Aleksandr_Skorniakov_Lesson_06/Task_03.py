from json import dump


def users_hobbies():
    users, hobbies, info = [], [], {}

    with open('users.csv', 'r', encoding='utf-8') as f:
        for i in f:
            users.append(i.strip().replace(',', ', '))

    with open('hobbies.csv', 'r', encoding='utf-8') as f:
        for i in f:
            hobbies.append(i.strip().replace(',', ', '))

    for i in range(len(users)):
        if i > len(hobbies) - 1:
            hobby = None
        else:
            hobby = hobbies[i]
        info.setdefault(users[i], hobby)

    print(info)

    with open('users_hobbies_03.txt', 'w', encoding='utf-8') as f:
        if 'None' not in info:
            dump(info, f, indent=4, ensure_ascii=False)
            f.write('\n')
        else:
            exit(1)


if __name__ == '__main__':
    users_hobbies()
