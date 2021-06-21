class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        return self.cell_number + other.cell_number

    def __sub__(self, other):
        return self.cell_number - other.cell_number if self.cell_number - other.cell_number >= 0\
            else 'Количество ячеек второй клетки привышает количество первой!'

    def __mul__(self, other):
        return self.cell_number * other.cell_number

    def __floordiv__(self, other):
        return self.cell_number // other.cell_number

    def make_order(self, row):
        return ('🦠' * row + '\n') * int(self.cell_number / row) + '🦠' * (self.cell_number % row)


cell_1 = Cell(18)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(3))
