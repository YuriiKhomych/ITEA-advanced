def bread(func):
    def wrapper():
        print()
        func()
        print("Toast")
    return wrapper


def ingredients(func):
    def wrapper():
        print("Tomato")
        func()
        print("Salad")
    return wrapper


@bread
@ingredients
def sandwich1(food="Ham"):
    print(food)


sandwich1()
