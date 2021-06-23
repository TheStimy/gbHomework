class ComplexNumber:
    def __init__(self, z_1, z_2):
        self.z_1 = z_1
        self.z_2 = z_2

    def __add__(self, other):
        return self.z_1 + other.z_2

    def __mul__(self, other):
        return self.z_1 * other.z_2


a, b = 3 + 1j, 2 - 3j
complex_number = ComplexNumber(a, b)
print('Addition -', a + b)
print('Multiplication -', a * b)
