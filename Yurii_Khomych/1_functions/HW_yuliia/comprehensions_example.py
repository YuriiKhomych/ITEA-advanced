#example 1
list1=[]
res= [x for x in range(1,40) if not x%2]
list1.extend(res)
print(list1)

#example 2
set1={1}
for y in range(10):
    set1.add(y*2)
print(set1)

