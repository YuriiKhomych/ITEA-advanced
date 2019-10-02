# from abc import ABCMeta, abstractclassmethod
#
# class BasePizza:
#     @abstractclassmethod
#     def margherita(cls):
#         pass
#
import math


class Pizza:
    def __init__(self, ingredients, radius):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls, radius):
        return cls(ingredients=['mozzarella', 'tomatoes'], radius=radius)

    @classmethod
    def prosciutto(cls):
        return cls(ingredients=['mozzarella', 'tomatoes', 'ham'], radius=30)

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

#
# Pizza(['mozzarella', 'tomatoes'])
# Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
# Pizza(['mozzarella'] * 4)
#
# Pizza(['cheese', 'tomatoes'])

margherita = Pizza.margherita()
prosciutto = Pizza.prosciutto()
x=3
