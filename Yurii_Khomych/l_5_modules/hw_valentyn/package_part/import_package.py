import car_for_package as c
#from .car_for_package import models
#from .car_for_package import tripled

if __name__ == "__main__":
    someCar = c.Car(c.models[1], "Green")
    print(someCar.model)

    print(c.tripled("Hello"))

