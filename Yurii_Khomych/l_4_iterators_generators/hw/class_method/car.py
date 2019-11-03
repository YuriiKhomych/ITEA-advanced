
class Car:

    def __init__(self, model, color="Red", engine="2"):
        self.model = model
        self.color = color
        self.engine = engine
        self.count_open_door = 0
        self.tank = 50

    def __repr__(self):
        return 'Car: Model: {!r}, Color: {!r} , Engine: {!r}'.format(self.model, self.color, self.engine)

    def open_door(self):
        print("Door was opened")
        self.count_open_door += 1
        self.tank -= 1

    def fill_the_tank(self):
        print("Tank was filled")
        self.tank = 50

    @classmethod
    def car_golf(cls):
        return cls('Golf', 'Red', 2.0)

    @classmethod
    def car_ford_mondeo(cls):
        return cls('Ford', 'White', 1.5)

    @staticmethod
    def tax_for_new_car(price):
        ret = price * .08
        return "You will pay taxes {!r}".format(ret)

    @staticmethod
    def count_full_price(price):
        ret = (price * .08 + price)
        return "You will pay for car with taxes {!r}".format(ret)


print(Car.count_full_price(100))
print(Car.tax_for_new_car(100))

print(Car.car_golf())
cad = Car.car_ford_mondeo()

cad.open_door()
cad.fill_the_tank()
