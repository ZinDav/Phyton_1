# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} машина {self.name} поехала')

    def stop(self):
        print(f'{self.color} машина {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Скорость {self.name} {self.speed}')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Скорость {self.name} {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(50, 'Серая', 'Toyota', False)
sport_car = SportCar(120, 'Красная', 'Lamborghini', False)
work_car = WorkCar(50, 'Зеленая', 'Kia', False)
police_car = PoliceCar(60, 'Черная', 'Volkswagen', True)

cars = [town_car, sport_car, work_car, police_car]
for c in cars:
    print(c.speed, c.color, c.name, c.is_police)
    c.go()
    c.stop()
    c.turn('направо')
    c.show_speed()
