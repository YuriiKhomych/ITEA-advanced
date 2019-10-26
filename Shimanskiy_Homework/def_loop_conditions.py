def something(list_1):
    l = []
    for i in list_1:
        if i > 2:
            x = i * 2
            l.append(x)
    return l


list_1 = [1, 2, 3, 4]
func = [i * 2 for i in list_1 if i > 2]
print(func)
print(something(list_1))

g = (lambda x: x ** 2)(2)
