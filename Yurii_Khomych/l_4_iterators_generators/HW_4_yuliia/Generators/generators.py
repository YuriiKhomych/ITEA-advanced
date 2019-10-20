# generator example 1
def example_1():
    my_list = []
    for x in range(10):
        my_list.append(x)
    return my_list


e = example_1()
print(e)

# generator statement example
e3 = [num*4 for num in range(5)]
print(e3)


# generator example 2
def example_2(value):
    for i in value:
        if i % 2:
            print('Index is ', i)
            yield i


for n in example_2([1, 2, 3, 4]):
    pass

