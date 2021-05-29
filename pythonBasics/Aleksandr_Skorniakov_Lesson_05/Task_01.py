def odd_nums(end):
    for odd in range(1, end + 1, 2):
        yield odd


n = 15
odd_to_n = odd_nums(n)

for i in range(1, n + 1, 2):
    print(next(odd_to_n))
