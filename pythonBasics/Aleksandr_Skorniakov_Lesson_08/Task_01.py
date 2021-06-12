import re


def email_parse(email):
    check_email = re.compile(r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$')
    if not check_email.match(email):
        raise ValueError(f'Wrong email - {email}')
    parse = re.compile(r'\w+[.]*\w+').findall(email)
    for i in range(len(parse)):
        values[keys[i]] = parse[i]
    print(values)


if __name__ == '__main__':
    keys = ['username', 'domain']
    values = {}
    try:
        email_parse('someone@geekbrains.ru')
    except ValueError as err:
        print(err)
