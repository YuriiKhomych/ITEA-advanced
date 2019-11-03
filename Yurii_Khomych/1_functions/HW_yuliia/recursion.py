#example 1
def recursion_ex1(x):
    if x==0:
        return x
    else:
        print(x)
        return recursion_ex1(x-1)

recursion_ex1(5)

#example 2
def recursion_ex2(a,b):
    if a<=b:
        return print(f'Value {a} less then {b}')
    else:
        print(a,b)
        return recursion_ex2(a-1,b+1)

recursion_ex2(10,0)






