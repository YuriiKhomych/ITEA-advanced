class SomeList(list):

    def __delitem__(self, index):
        self.pop(index)

    def __add__(self, other):
        self.append(other)

    def __eq__(self, other):
        return super().__eq__(other)

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"


x = SomeList([2, 1, 3, 4])
y = SomeList([1, 2, 3, 5])
print(x)
del x[0]
x.__add__(6)
print(x)
del y[1]
del x[-1]
del y[-1]

print(x == y)
del x[-1]
print(x == y)

print(x != y)
