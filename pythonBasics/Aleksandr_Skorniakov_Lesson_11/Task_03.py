class OnlyNums(Exception):
    pass


lst = []

while True:
    lst.append(input('Enter number: '))

    if lst[-1] == 'stop':
        print(lst[:-1])
        break

    try:
        if lst[-1].isdigit():
            int(lst[-1])
        else:
            lst.pop(-1)
            raise OnlyNums
    except OnlyNums:
        print("List may contain only numbers")
