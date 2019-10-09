# example 1
Car = type('Car', (), {'wheels': 4, 'engine': 1.6})
print(Car)
print(hasattr(Car, 'engine'))

# example 2
Motorcycles = type('Bicycle', (Car,), {'wheels': 2})
print(Motorcycles)
print(hasattr(Motorcycles, 'doors'))
print(hasattr(Motorcycles, 'engine'))
print(Motorcycles.mro())
