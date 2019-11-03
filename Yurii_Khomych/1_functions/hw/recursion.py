import random


# ***** bubble Sorting
def bubble_sort(list_t):
    for pos, num in enumerate(list_t):
        try:
            if list_t[pos + 1] < num:
                list_t[pos] = list_t[pos + 1]
                list_t[pos + 1] = num
                bubble_sort(list_t)
        except IndexError:
            pass
    return list_t


sortList = [random.randint(-10, 100) for x in range(10)]

print("array:")
for i in range(0, len(sortList)):
    print(sortList[i], end=' ')

bubble_sort(sortList)

print("\nSorted array:")
for i in range(0, len(sortList)):
    print(sortList[i], end=' ')


# ****** FACTORIAL
def factorial(number_f):
    if number_f != 1:
        return number_f * factorial(number_f - 1)
    else:
        return number_f


print('\nFactorial: ', factorial(9))
