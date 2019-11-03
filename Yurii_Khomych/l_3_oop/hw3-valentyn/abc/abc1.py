from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def fill_the_tank(self):
        pass


class Tesla(Car):
    def __init__(self, version=0, tank=50):
        self.version = version
        self.tank = tank

    def update(self):
        self.version += 1

    def fill_the_tank(self, v):
        self.tank += v


C = Tesla()

C.fill_the_tank(1)
print(C.tank)
