def checker(calc_cube_f):
    def _val_checker(val_func):
        def wrapper(val):
            if calc_cube_f(val):
                print(val_func(val))
            else:
                raise ValueError(f'Wrong value: {val}')

        return wrapper

    return _val_checker


@checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
except ValueError as err:
    print(err)
