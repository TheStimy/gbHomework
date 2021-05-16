goods = [23.74, 95.43, 41.85, 76.01, 50.91, 21.38, 93.14, 42.53, 19.43, 73.24]

for i in range(len(goods)):
    print(int(goods[i] // 1), 'руб.', "%02.f" % int(goods[i] * 100 % 100), 'коп.', end=', ')
print()

goods.sort()

for i in range(len(goods)):
    print(int(goods[i] // 1), 'руб.', "%02.f" % int(goods[i] * 100 % 100), 'коп.', end=', ')
print()

goods.reverse()

for i in range(len(goods)):
    print(int(goods[i] // 1), 'руб.', "%02.f" % int(goods[i] * 100 % 100), 'коп.', end=', ')
print()

goods.sort()

for i in range(len(goods) - 5, len(goods)):
    print(int(goods[i] // 1), 'руб.', "%02.f" % int(goods[i] * 100 % 100), 'коп.', end=', ')
print()
