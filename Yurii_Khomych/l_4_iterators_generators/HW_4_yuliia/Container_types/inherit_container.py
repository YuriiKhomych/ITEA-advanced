# inherited dict


class DictNew(dict):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.my_dict = {key: value}

    def create_dict(self):
        return self.my_dict


film1 = DictNew('actor', 'Richard Gir', 'Jonas Hill')
film2 = DictNew('actor', 'Bradley Cooper', 'Jonas Hill')
print(film1.create_dict())
print(film2.create_dict().pop('actor'))



