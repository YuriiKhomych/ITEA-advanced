print({x for x in range(-9, 10)})
print({x: x ** 3 for x in range(5)})

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:", list_using_comp)