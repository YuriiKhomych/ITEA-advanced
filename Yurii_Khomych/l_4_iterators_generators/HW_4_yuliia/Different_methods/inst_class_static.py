class Universe:
    def __init__(self, *planets):
        self.planets = planets

# class method
    @classmethod
    def is_life_there(cls):
        return cls('Earth')

    @classmethod
    def possible_home(cls):
        return cls('Mars')

# instance method
    def what_is_it(self):
        print(f'This is {list(self.planets)}')

# static method
    @staticmethod
    def how_many(*p):
        count = 0
        for i in p:
            count = count+1
        return print(count)


Universe.is_life_there()
Universe.possible_home()
Universe('Saturn').what_is_it()
Universe().how_many('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')


