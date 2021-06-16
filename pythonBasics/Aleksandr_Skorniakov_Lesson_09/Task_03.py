class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'

    def get_total_income(self):
        return f'{self.position}s income - {sum(self._income.values())}$'


worker = Position('Ryan', 'Gosling', 'Actor', 15000000, 2000000)

print(worker.get_full_name())
print(worker.get_total_income())
