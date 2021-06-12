from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args):
        string = []
        for i in range(len(args)):
            string.append(str(args[i]) + ': ' + str(type(args[i])))
        print(str(func.__name__) + '(' + str(string)[1:-1] + ')', sep=', ')
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube)
calc_cube(5, 6, 9)
