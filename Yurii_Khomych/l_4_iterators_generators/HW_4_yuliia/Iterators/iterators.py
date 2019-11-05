# some example with iteration by 2
class Custom:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        self.value += 2
        return self.value


d = Custom(10)
print(d.__next__())
print(d.__next__())
print(d.__next__())


# some example 2 with overwritten method iter to return reversed iteration
class GoTo:
    def __init__(self, *some_var):
        self.some_var = list(some_var)

    def __iter__(self):
        temp = len(self.some_var)
        if temp < 0:
            raise StopIteration
        else:
            temp -= 1
            return self.some_var.pop(temp)


sense = GoTo('What', 42, 'is', 24, 'life', 42)
print(sense.__iter__())
print(sense.__iter__())
