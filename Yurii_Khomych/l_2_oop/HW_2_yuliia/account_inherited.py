import copy


# base Class
class Country:
    def __init__(self, name, area, continent='Europe'):
        self.name = name
        # area will shown in kilometers
        self.area = area
        self.continent = continent
        self.cities = []

    # create list with City names
    def __add__(self, *cities):
        if cities not in cities:
            self.cities.extend(cities)
        return self.cities

    # Information about what place is it
    def show_info(self):
        return f'This is {self.name}'

    # example of usage shallow and deep copy
    def which_ocean(self):
        oceans = {'ocean': ['Pacific', 'Arctic', 'Southern']}
        if self.continent in ['South America']:
            oceans_south = copy.copy(oceans)
            print(oceans_south)
        elif self.continent in ['North America']:
            oceans_south = copy.copy(oceans)
            oceans_south['ocean'][2]='Atlantic'
            print(oceans_south)
            if oceans == oceans_south:
                print('Ooops, shallow copy!')
            else:
                print('looks like a deep copy')

        elif self.continent in ['Europe']:
            oceans_eu = copy.deepcopy(oceans)
            oceans_eu['ocean'][0]='Atlantic'
            oceans_eu['ocean'].pop(2)
            print(oceans_eu)
            if oceans != oceans_eu:
                print("Congratulations! it's a deep copy")
            else:
                print('please check your copy')


# child class
class City(Country):
    def __init__(self, name):
        super().__init__(name, name)

    # create a dict with City name as key to show city population
    def city_population_add(self, *people_amount):
            city_population = {}
            for x in range(len(self.cities)):
                city_population[self.cities[x]] = people_amount[x]
            return city_population


# examples
a = Country('Spain', 505990, 'Europe')
a.which_ocean()
b = City('Spain')
b.__add__('Barcelona', 'Madrid', 'Malaga', 'Valencia')
print(b.city_population_add(1615000, 3174000, 569005, 789004))
print(b.show_info())

a = Country('USA', 9834000, 'North America')
a.which_ocean()
b = City('USA')
b.__add__('El Paso', 'Orlando', 'LA')
print(b.city_population_add(683577, 280257, 4000000))
print(b.show_info())
print(City.mro())





