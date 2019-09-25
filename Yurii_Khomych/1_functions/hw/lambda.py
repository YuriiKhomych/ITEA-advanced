def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc( 2 )
print( mydoubler( 11 ) )

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print( full_name( 'guido', 'van rossum' ) )

sum1 = lambda first, last: first + last
print( sum1( '123', '345' ) )
