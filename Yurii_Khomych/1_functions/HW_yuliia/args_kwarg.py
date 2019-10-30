#args example
def example_1(*args):
    my_var=[]
    for x in args:
        my_var.extend(args)
        if len(my_var) == len(args):
            break
    return my_var
print(example_1('Tunder','lightning'))
print(example_1('Mature','Rebellious',1,2))

#kwargs example
def example_2(**kwargs):
    my_var2={}
    for x in kwargs.items():
        my_var2.update(kwargs.items())
    return my_var2

print(example_2(a="altron",b="batman",c="captain america",d='dark panther'))

