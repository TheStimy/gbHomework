filter_by_name = {}


def thesaurus(*args):
    for arg in args:
        filter_by_name[arg[0]] = [name for ind, name in enumerate(args) if name[0] == arg[0]]
    print(filter_by_name)


thesaurus("Иван", "Мария", "Петр", "Илья")
