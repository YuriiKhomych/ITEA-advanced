class Car( type ):
    def __init__(cls, *arg):
        cls.wheels = 4
        cls.engine = 1
        cls.doors = 5
        cls.airbags = 2
        cls.seatbelt = 5


class VW( metaclass=Car ):
    def __init__(self, a, b, c, d, e):
        self.wheels = a
        self.engine = b
        self.doors = c
        self.airbags = d
        self.seatbelt = e

    def safety(self):
        return self.airbags + self.seatbelt


class ElectroCar( metaclass=Car ):

    def __init__(self, a):
        self.kmPerOneCharge = a


suicideCar = VW( 1, 2, 3, 4, 9 )
suicideCar2 = ElectroCar( 100 )
print( suicideCar.safety() )
print( suicideCar.seatbelt )
print( suicideCar2.seatbelt, suicideCar2.kmPerOneCharge )
