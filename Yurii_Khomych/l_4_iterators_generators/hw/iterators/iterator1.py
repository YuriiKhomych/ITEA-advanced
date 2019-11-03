# first example
class UserRangeReverse:
    def __init__(self, n):
        self.i = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 0:
            i = self.i
            self.i -= 1
            return i
        else:
            raise StopIteration()


ur_reverse = UserRangeReverse(5)
print(list(ur_reverse))
