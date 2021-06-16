import random


def decoration():
    print('*' * 10)


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} в движении!')

    def stop(self):
        print(f'{self.color} {self.name} стоит!')

    def turn_direction(self):
        print(f'{self.name} повернул на {"лево" if random.randint(0, 1) == 0 else "право"}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} км/ч')

    def police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина!')
        else:
            print(f'{self.name} гражданская машина!')


class TownCar(Car):
    def speed_limit(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость!')
        elif self.speed < 40:
            print(f'{self.name} едет слишком медленно!')
        else:
            print(f'Скорость {self.name} в норме!')


class SportCar(Car):
    def speed_limit(self):
        if self.speed > 110:
            print(f'{self.name} превышает скорость!')
        elif self.speed < 90:
            print(f'{self.name} едет слишком медленно!')
        else:
            print('Скорость в норме!')


class WorkCar(Car):
    def speed_limit(self):
        if self.speed > 50:
            print(f'{self.name} превышает скорость!')
        elif self.speed < 30:
            print(f'{self.name} едет слишком медленно!')
        else:
            print('Скорость в норме!')


class PoliceCar(Car):
    def speed_limit(self):
        if self.speed > 70:
            print(f'{self.name} превышает скорость!')
        elif self.speed < 50:
            print(f'{self.name} едет слишком медленно!')
        else:
            print('Скорость в норме!')


town_car = TownCar(random.randint(30, 70), 'Синяя', 'BMW', False)
sport_car = SportCar(random.randint(80, 120), 'Красная', 'Bugatti', False)
work_car = WorkCar(random.randint(20, 60), 'Черный', 'Nissan', False)
police_car = PoliceCar(random.randint(40, 80), 'Белый', 'Ford', True)


car_func = [town_car, sport_car, work_car, police_car]

for car in car_func:
    decoration()
    car.go()
    car.stop()
    car.turn_direction()
    car.show_speed()
    car.speed_limit()
    car.police()
