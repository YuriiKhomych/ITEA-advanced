import random

#### ***** buble Sorting
def bubble_sort(listt):
    for i, num in enumerate( listt ):
        try:
            if listt[i + 1] < num:
                listt[i] = listt[i + 1]
                listt[i + 1] = num
                bubble_sort( listt )
        except IndexError:
            pass
    return listt


sortList = [random.randint( -10, 100 ) for x in range( 10 )]

print( "array:" )
for i in range( 0, len( sortList ) ):
    print( sortList[i], end=' ' )

bubble_sort( sortList )

print( "\nSorted array:" )
for i in range( 0, len( sortList ) ):
    print( sortList[i], end=' ' )

#### ****** FACTORIAL
def factorial(numberF):
    if numberF != 1:
        return numberF * factorial( numberF - 1 )
    else:
        return numberF


print( '\nFactorial: ', factorial( 9 ) )
