a = [[5, 9, 2], [8, 1, 4], [6, 2, 3]]
b = [[8, 2, 7], [3, 6, 1], [9, 5, 4]]


class Matrix:
    def __init__(self, m_data):
        self.m_data = m_data

    def __str__(self):
        matrix = ''
        for line in self.m_data:
            for number in line:
                matrix += '\t' + str(number)
            matrix += '\n'
        return matrix

    def __add__(self, other):
        matrix_c = []
        for nr_line, line_line in enumerate(self.m_data):
            matrix_c.append([])
            for nr_number, line_number in enumerate(line_line):
                matrix_c[nr_line].append(line_number + other.m_data[nr_line][nr_number])
        self.m_data = matrix_c
        return self.__str__()


matrix_a = Matrix(a)
matrix_b = Matrix(b)
print('Matrix A -\n' + str(matrix_a))
print('Matrix B -\n' + str(matrix_b))
print('Matrix C -\n' + str(matrix_a + matrix_b))
