
x="XX"
try:
    print(x+"x")
except TypeError as t:
    print('Type error')
except NameError as n:
    print("Name Error")
except Exception as e:
    print("General exeption")
else:
    print("No Exceptions")
finally:
    print("Always lock the laptop")