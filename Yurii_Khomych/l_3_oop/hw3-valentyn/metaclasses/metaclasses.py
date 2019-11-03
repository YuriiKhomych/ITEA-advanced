class Car(type):
    def __init__(cls, *arg):
        cls.wheels = 4
        cls.engine = 1
        cls.doors = 5
        cls.airbags = 2
        cls.seat_belt = 5


class VW(metaclass=Car):
    def __init__(self, a, b, c, d, e):
        self.wheels = a
        self.engine = b
        self.doors = c
        self.airbags = d
        self.seat_belt = e

    def safety(self):
        return self.airbags + self.seat_belt


class GreenCar(metaclass=Car):

    def __init__(self, a):
        self.kmPerOneCharge = a


suicideCar = VW(1, 2, 3, 4, 9)
suicideCar2 = GreenCar(100)
print(suicideCar.safety())
print(suicideCar.seat_belt)
print(suicideCar2.seat_belt, suicideCar2.kmPerOneCharge)
