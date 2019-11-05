# generator example 1
def example_1():
    my_list = []
    for argument in range(10):
        my_list.append(argument)
    print(my_list)
    yield my_list


result = example_1()
print(result)

# generator example
result2 = (num*4 for num in range(5))
print(result2)


# generator example 2
def example_2(value):
    for attribute in value:
        if attribute % 2:
            print('Index is ', attribute)
            yield attribute


for number in example_2([1, 2, 3, 4]):
    pass

