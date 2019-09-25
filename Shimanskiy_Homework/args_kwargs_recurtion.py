def found_letter(*args):
    for i in args:
        try:
            if i == 0:
                d = args.count(i)
        except UnboundLocalError:
            pass
        else:
            if i == 1:
                d = args.count(i)
        return d


print(found_letter(1, 2, 2, 1, 3, 4, 6, 1))


def find_value(**kwargs):
    l = []
    for i in kwargs.keys():# something strange, it work wrong it make kwargs as Key???
        l.append(i)
    for j in kwargs.values(): # not value just all dict
        pass

    return l, j

    #kwargs = {**dict_1, **dict_2, **kwargs} some experiment it does not work




dict_1 = {'a': 1, 'b': 23, 'c': 'kj'}
dict_2 = {'a': 31, 'b': 11, 'k': 'word wide'}
some_dict = {**dict_1, **dict_2}
print(some_dict)

print(find_value(kwargs=some_dict))
