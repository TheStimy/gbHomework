print([sum(map(int, str(x ** 3))) for x in range(1, 1000, 2) if sum(map(int, str(x ** 3))) % 7 == 0])
print([sum(map(int, str(x ** 3 + 17))) for x in range(1, 1000, 2) if sum(map(int, str(x ** 3 + 17))) % 7 == 0])
