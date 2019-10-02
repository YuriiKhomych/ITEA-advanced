import time
from contextlib import contextmanager

a = 10
b = 0
c = 3


#
def suma_b(a, b):
    return a / b


#?????????????????????????????????
@contextmanager
def single(c):
    print( "Starting" )
    yield()
    print( "Finishin" )


#
#
single( c )


# Python program creating a
# context manager
##

##exceptions
class ContextManagerException():
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type == self.exc_type:
            print( 'Caught exception' )
            return True


with ContextManagerException( ZeroDivisionError ):
    suma_b( a, b )


##timer
class timer():
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        print( "Time spent", time.time() - self.start )


with timer():
    time.sleep( 2 )
