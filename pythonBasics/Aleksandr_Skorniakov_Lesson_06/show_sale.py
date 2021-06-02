import sys
from sys import argv


def show_sale(start=0, stop=0, flag=0):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if flag == 0:
            print(*(sale.strip() for sale in f), sep='\n')
        elif flag == 1:
            print(*(line.strip() for i, line in enumerate(f) if start <= i), sep='\n')
        elif flag == 2:
            print(*(line.strip() for i, line in enumerate(f) if start <= i <= stop), sep='\n')
        '''Второй вариант с использаванием метода seek()'''
        # elif flag == 1:
        #     f.seek(7 * start)
        #     print(*(line.strip() for line in f), sep='\n')
        # elif flag == 2:
        #     f.seek(7 * start)
        #     print(*(line.strip() for i, line in enumerate(f) if i <= stop), sep='\n')


if __name__ == '__name__':
    if len(sys.argv) == 1:
        show_sale(flag=0)

    elif len(sys.argv) == 2:
        show_sale(int(argv[1]) - 1, stop=0, flag=1)

    elif len(sys.argv) == 3:
        show_sale(int(argv[1]) - 1, int(argv[2]) - 1, flag=2)
