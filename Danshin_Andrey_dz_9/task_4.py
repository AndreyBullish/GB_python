class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name


    def go(self) -> None:
        speed_plus_15 = self.speed + 15
        result = f'Машина {self.name} повысила скорость на 15: {speed_plus_15}'
        return print(result)


    def stop(self) -> None:
        self.speed = self.speed - self.speed
        print(f'{self.name} остановилась')


    def turn(self, direction: str) -> None:
        self.direction = direction
        if direction == 'направо' or direction == 'налево' or direction == 'прямо' or direction == 'назад':
            print(f'{self.name}({self.__class__.__name__}): движется {direction}')
        else:
            raise ValueError('нераспознаное направление движения')


    def show_speed(self) -> None:
        print(f'{self.name}: текущая скорость {self.speed} км/час')


# # определите классы TownCar, WorkCar, SportCar, PoliceCar согласно условия задания
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed} км/час')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed} км/час')

class SportCar(Car):
    pass

class PoliceCar(Car):
    is_police = True
    def show_speed(self):
        if self.is_police == True:
            print(f'{self.name}: текущая скорость {self.speed} км/час')
            print('Вруби мигалку и забудь про скорость!')


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # # BMW: текущая скорость 120 км/час
    # # Вруби мигалку и забудь про скорость!
    sport_car.turn('прямо')  # Ferrari(SportCar): движется назад
    # sport_car.turn('right')
    # """
    # Traceback (most recent call last):
    #   ...
    # ValueError: нераспознанное направление движения
    # """