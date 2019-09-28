from functools import reduce

zip_obj = zip([1, 2, 3], ['a', 'b', 'c'], ["x", "y", "z"])

filter_res = filter(lambda x: x % 2 != 0, [1, 3, 10, 45, 6, 50])
filter_comp = [x for x in [1, 3, 10, 45, 6, 50] if x % 2 != 0]
filter_gen = (x for x in [1, 3, 10, 45, 6, 50] if x % 2 != 0)


map_res = map(lambda x: x + x, [1, 3, 10, 45, 6, 50])

my_list = [1, 2, 3, 4, 5]
reduce_res = reduce(lambda x, y: x * y, my_list)

pass