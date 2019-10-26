from abc import ABCMeta, abstractmethod


class BankAccount(metaclass=ABCMeta):
    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def get_amount(self):
        pass


class Bank1(BankAccount):
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount

    def get_number(self):
        return self.number

    def get_amount(self):
        return self.amount


class Bank2(BankAccount):
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount

    def get_number(self):
        return self.number

    def get_amount(self):
        return self.amount * 0.95


B1 = Bank1(111, 100)
B2 = Bank2(111, 100)


print(B1.get_amount())
print(B2.get_amount())
