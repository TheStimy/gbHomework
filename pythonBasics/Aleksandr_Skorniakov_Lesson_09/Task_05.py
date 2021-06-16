class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title[:-1].lower()}ой')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title.lower()}ом')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title.lower()}ом')


stationery = Stationery()
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()

