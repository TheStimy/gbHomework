goods = [23.74, 95.43, 41.85, 76.01, 50.91, 21.38, 93.14, 42.53, 19.43, 73.24]


def goods_function(number_of_goods):
    for i in number_of_goods:
        print(int(goods[i] // 1), 'руб.', "%02.f" % int(goods[i] * 100 % 100), 'коп.', end=', ')
    print()


goods_function(range(len(goods)))

goods.sort()

goods_function(range(len(goods)))

goods.reverse()

goods_function(range(len(goods)))

goods.sort()

goods_function(range(len(goods) - 5, len(goods)))
