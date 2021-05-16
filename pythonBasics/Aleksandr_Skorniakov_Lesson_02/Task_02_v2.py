import re

input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
element_place = 0

while element_place < len(input_list):
    if input_list[element_place].lstrip('+-').isdigit():
        if input_list[element_place][0] in '+-':
            input_list[element_place] = input_list[element_place].zfill(3)
        else:
            input_list[element_place] = input_list[element_place].zfill(2)
        input_list.insert(element_place, '"')
        input_list.insert(element_place + 2, '"')
        element_place += 2
    element_place += 1

print(input_list)

input_list = ' '.join(input_list)
input_list = re.sub(r'"\s*([^"]*?)\s*"', r'"\1"', input_list)   # Использовал regex только ради опыта и разнообразия

print(input_list)
