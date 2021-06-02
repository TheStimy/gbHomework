from sys import argv


def rewrite_sale(position, sale):
    with open('bakery.csv', 'a', encoding='utf-8') as cursor:
        cursor.seek(cursor.tell() - 7)
        if cursor.tell() < cursor.seek(7 * position):
            exit(1)
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        f.seek(7 * position)
        f.write(sale + '\n')


rewrite_sale(int(argv[1]) - 1, argv[2])
