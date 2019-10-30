#loop example 1
str1='hello'
list1=['Oleg','Vasia','Andrii']
while len(list1) > 0:
    print(str1+' '+list1[0])
    list1.remove(list1[0])

#loop example 2
str2='Perception'
list2=[]
list2.extend(str2)
for x in list2:
    list2.pop(0)
print(list2)


