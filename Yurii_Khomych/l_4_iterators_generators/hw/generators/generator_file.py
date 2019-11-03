# function generator
def list_generator(start, end):
    while start <= end:
        yield start
        start += 1


n_list = []
for num in list_generator(1, 10):
    n_list.append(num)

print(n_list)

# generator 2
cube_list = (x ** 3 for x in range(1, 10))
print(type(cube_list))
print(list(cube_list))


# generator 3
def odd_number(value):
    for i in value:
        if i % 2 != 0:
            yield i


for n in odd_number(range(1, 10)):
    print(n)
