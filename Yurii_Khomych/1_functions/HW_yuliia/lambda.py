#example 1
alcohol_allowed=lambda age,document:age>21 or document is True
print(alcohol_allowed(22,False))

#example 2
str1=lambda a='',b='': print(a.capitalize()+' '+b.lower())
str1('GOOD','MORNING')