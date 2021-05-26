def thesaurus_adv(*args):
    filter_by_name = {}
    for full_name in args:
        name, surname = full_name.split()
        int_val = filter_by_name.setdefault(surname[0], {name[0]: [full_name]})
        int_key = int_val.setdefault(name[0], [full_name])
        if full_name not in int_key:
            int_key.append(full_name)
    print(filter_by_name)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
