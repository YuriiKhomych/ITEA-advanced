from collections import UserList


class SomeList(UserList):

    def __setitem__(self, index, item):
        if index == len(self.data):
            self.data.append(item)
        else:
            self.data[index] = item


list_users = SomeList()

for i in range(10):
    list_users[i] = i

list_users[10] = 11
print(list_users)
