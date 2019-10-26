b1 = 6


def f11(a):
    print(a)
    print(b1)

    def f2():
        c = a + b1
        return c * 3

    return f2()


print(f11(3))

a = 5


def function():
    global a
    print(a)
    a = 10
    print(a)


function()
print(a)


def f1():
    a = 1
    b = 2

    def f2():
        nonlocal a
        a += b
        return a

    return f2()


print(f1())
