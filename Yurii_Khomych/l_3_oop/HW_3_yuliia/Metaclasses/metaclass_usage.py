# example 1
class Car(type):
    def __new__(cls, name, bases, dct):
        result = super().__new__(cls, name, bases, dct)
        result.engine = 1.6
        return result


class Ford(metaclass=Car):
    pass


class Skoda(metaclass=Car):
    pass


class Hundai(metaclass=Car):
    pass


print(Hundai.engine)
print(Skoda.engine)
print(Ford.engine)


# example 2
question = input("Do you have engine?")
if question.lower() == "y":
    car = True
else:
    car = False
    print('Sorry, here was a stupid one who can predict only two options')


def who_am_i(self):
    answer = 'You are a car!'
    return answer


class YourAnswer(type):

    def __init__(cls, name, bases, dct):
        if car:
            cls.who_am_i = who_am_i
        else:
            quit()


class Undefined1(metaclass=YourAnswer):
    pass


class Undefined2(metaclass=YourAnswer):
    pass


mazda = Undefined1()
print(mazda.who_am_i())
