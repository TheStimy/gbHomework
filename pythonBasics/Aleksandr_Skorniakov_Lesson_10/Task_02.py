from abc import ABC, abstractmethod


class Cloth(ABC):
    final = 0

    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def material_usage(self):
        pass

    def __add__(self, other):
        Cloth.final += self.material_usage + other.material_usage
        return Costume(0)

    def __str__(self):
        materials = Cloth.final
        Cloth.final = 0
        return f'{materials}'


class Coat(Cloth):
    @property
    def material_usage(self):
        return int(self.size / 6.5 + 0.5)


class Costume(Cloth):
    @property
    def material_usage(self):
        return int((2 * self.size + 0.3) / 100)


coat = Coat(110)
costume = Costume(180)
print(coat + costume)
