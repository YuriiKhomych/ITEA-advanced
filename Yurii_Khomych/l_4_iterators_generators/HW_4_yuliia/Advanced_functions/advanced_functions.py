from functools import reduce


# map example
def create_dict(x, y):
    result = {x: y}
    return result


a = map(create_dict, [1, 2, 3], [4, 5, 6])
print(a.__next__())

# filter example
b = filter(lambda n: n*n > 0, [1, 2, 3, 0])

# reduce example
c = reduce(lambda m, l: m*l, [1, 2, 3])

# zip example
d = zip(['red', 'blue', 'green'], [100, 200, 300])
print(d.__next__())

