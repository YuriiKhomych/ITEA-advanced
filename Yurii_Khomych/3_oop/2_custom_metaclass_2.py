class Meta(type):
    def __new__(cls, name, bases, dct):
        result = super().__new__(cls, name, bases, dct)
        result.attr = 100
        return result

    # def __init__(self, name):
    #     self.name = name


class Foo(metaclass=Meta):
    pass


class Bar(metaclass=Meta):
    pass


class Qux(metaclass=Meta):
    pass


print(Foo.attr)
print(Bar.attr, Qux.attr)

