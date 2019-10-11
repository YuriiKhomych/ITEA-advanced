# * Datatypes (2-3 examples of each data type)
is_rain = False
if not is_rain:
    print("it is not rain")
else:
    print("it is rain")
is_night = True
if is_night:
    print("Go to bed")

number1_int = 2
number2_int = 4

number1_float = 2.8
number2_float = 3.5

str1 = "qwerty"
str2 = (str(number1_float) + "3") * 4
print(str2)

list1 = [1, 2, 3, 2, 4, 5]

print(list1)
list1.append(6)
list1.pop(3)
print(list1)

tuple1 = (1, 2, 3, 4, 5, 5, 2, 2)
print(tuple1)
tuple2 = tuple1 + (222, 333)
print(tuple1.count(2))
print(tuple2)

set1 = {1, 2, 3, 4}
set1.add(2)
set1.add("22")
print(set1)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1.keys())
print(dict1.get('c'))
