odd_in_cube = [x ** 3 for x in range(1, 1000, 2)]
result = []


def sum_of_digits_function(single_number):
    sum_of_digits = 0
    while single_number:
        sum_of_digits += single_number % 10
        single_number //= 10
    return sum_of_digits


def sum_and_div_function():
    result.clear()
    for single_number in odd_in_cube:
        if sum_of_digits_function(single_number) % 7 == 0:
            result.append(sum_of_digits_function(single_number))
    print(result)


sum_and_div_function()

odd_in_cube = [x + 17 for x in odd_in_cube]

sum_and_div_function()
