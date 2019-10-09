from abc import ABC
# example 1


class Animal(ABC):
    # abstract method
    def can_say(self):
        pass


class Cat(Animal):
    def can_say(self):
        print('Meoooow!')


class Dog(Animal):
    def can_say(self):
        print('Woof!')


class Fish(Animal):
    def can_say(self):
        print("I'm too quite and will die in a silence")


dorry = Fish()
dorry.can_say()


# example 2


class HouseElf(ABC):
    def owner(self):
        pass


class Kreacher(HouseElf):
    def owner(self):
        print('\r\n Kreacher, the Black family house-elf')


class Dobby(HouseElf):
    def owner(self):
        print('\r\n Dobby is a free house-elf, being freed from Malfoy family ')


Dobby().owner()
Kreacher().owner()