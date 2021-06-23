class ZeroError(Exception):
    pass


numerator = int(input('Enter numerator: '))
denominator = int(input('Enter denominator: '))

try:
    raise ZeroError if denominator == 0 else print(numerator / denominator)
except ZeroError:
    print("Can't be divided by zero")
