a=['red','yellow','green','blue']
b=['black','orange']
try:
    a.remove('black')
except:
    print('there is no such element in list')
    a.extend(b)
else:
    a.append(['grey'])
finally:
    print(a)
