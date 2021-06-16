class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_road(self):
        __mass = 25
        __thickness = 5
        return f'{self._length} m * {self._width} m * {__mass} kg * {__thickness} cm = ' \
               f'{int(self._length * self._width * __mass * __thickness / 1000)} t'


road = Road(5000, 20)
print(road.calc_road())
