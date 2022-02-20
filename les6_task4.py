class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} двигается'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул на право'

    def turn_left(self):
        return f'{self.name} повернул на лево'

    def show_speed(self):
        return f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч'
class TownCar(Car):
    speed_max = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.speed_max:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч')

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    MAX_SPEED = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

sc = SportCar(100, 'Red', 'Audi RS4')
tc = TownCar(150, 'White', 'LadA')
wc = WorkCar(30, 'Yeloow', 'CAT')
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(ford.name, ford.color, ford.speed, ford.is_police)
print(wc.go(), wc.turn_left(), wc.turn_right(), wc.stop())
print(tc.show_speed())
