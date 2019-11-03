from functools import reduce

# filter example
odd_number = filter(lambda n: n % 2 > 0, range(0, 11))
print(list(odd_number))

# reduce example
sum_number = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(sum_number)

# zip example
d = zip(['win', 'defeat', 'draw'], [3, 0, 1])
print(list(d))
