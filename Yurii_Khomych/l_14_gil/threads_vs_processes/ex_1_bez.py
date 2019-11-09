import threading
import random
import time
from functools import reduce


def func(number):
    random_list = random.sample(range(1000000), number)
    return reduce(lambda x, y: x * y, random_list)

if __name__ == '__main__':
    starttime = time.time()
    number = 500000
    func(number=number)
    print('That took {} seconds'.format(time.time() - starttime))
