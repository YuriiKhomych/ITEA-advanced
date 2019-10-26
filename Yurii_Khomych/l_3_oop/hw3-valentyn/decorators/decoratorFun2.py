def do_twice(func):
    print("first row")

    def wrapper(a):
        func(a+a)
        func(a)
    return wrapper


@do_twice
def func1(a):
    print(a)


func1("Hello")
