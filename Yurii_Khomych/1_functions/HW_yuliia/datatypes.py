#None
x=None
y=0
if x is None:
    print("It is a None type")
if y is not None:
    print("It is another type")

#bool datatype
a=True
b=False
if 2 <=2:
    print(a)
else:
    print(b)

#numbers
num1 = 10
num2 = 1.2
if num1>num2:
    print("Integer is grater then float")
print("And we can summarize them ",num1+num2)

#Strings
str1 = "Do not worry"
str2 = "Have a good day"
print(str1[:2]+" "+str2[5:])
print(f'Hi {str1}, lets play the game')

#list
list1=['how', 'you', ['are','doing']]
print(list1[0]+" "+list1[2][0]+" "+list1[1]+" "+list1[2][1])
list1.append('?')
print(list1)

#tuple
t1=("tuple",2,3,5)
if 2 in t1:
    print("2 is there")
    print(len(t1))

#set
set1={'rain','cloud','sky'}
if 'rain' in set1:
    print("rain in this set")
set1.update(['today','tomorrow'])
print(set1)
set2={'fog','rain'}
print(set1.union(set2))

#Dictionary
book={'book_name':'It','author':'Stephen King','year':'1986'}
print(book['book_name'])
book['book_name']='The end of the whole Mess'
print(book)
for x in book.values():
    print(x)


