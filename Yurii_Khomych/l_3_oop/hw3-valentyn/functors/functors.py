class FunctorClass(object):
    def do_something(self, x):
        if x.isdigit():
            return self.__pow(x)

        if type(x) is str:
            return self.__duplicate(x)

    @staticmethod
    def __pow(a):
        print("Pow 2")
        return int(a) ** 2

    @staticmethod
    def __duplicate(b):
        print("Duplicate")
        return b * 2


# string *2 number ^2
TestFunctor = FunctorClass()
y = input("Please input word or integer number: ")
print(TestFunctor.do_something(y))
