def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


n = 5
print(factorial_recursive(n))

list_1 = [['1', '2', '3'], ['1', '5', '9'], ['12', '111', '11']]


def count_element(list_1):
    count = 0
    for i in list_1:
        for j in i:
            if len(j) == 1:
                count += 1
            else:
                some_doing = list_1.replace([i][j], '1')
                count_element(some_doing)
    return count




count_element(list_1)