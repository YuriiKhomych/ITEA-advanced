def some_ex1(a, b, *args, **kwargs):
    print("First parameter: ", a)
    print("Second parameter: ", b)
    print("first args: ", args[0])
    print("Kwargs ", {x for x in kwargs.values()})


list1 = [1, 2, 3]
some_ex1('aaaaaa', 'bbbbbbb', *list1, **{'1': 1, '2': 2, "3": 3})


def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result


list2 = [4, 5]
list3 = [6, 7, 8, 9]
print(my_sum(*list1, *list2, *list3))
