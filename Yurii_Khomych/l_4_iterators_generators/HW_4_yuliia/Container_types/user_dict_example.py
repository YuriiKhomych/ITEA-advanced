from collections import UserDict


class MyDict(UserDict):
    def __init__(self):
        self.data = {}
        self['size'] = 0
        self['color'] = ''
        self['name'] = ''


b = MyDict()
b['size'] = 12
b['color'] = 'red'
b['name'] = 'socks'
print(b)







