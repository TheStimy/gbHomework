from sys import argv


def add_sale(sale):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(sale + '\n')


if __name__ == '__name__':
    add_sale(argv[1])
