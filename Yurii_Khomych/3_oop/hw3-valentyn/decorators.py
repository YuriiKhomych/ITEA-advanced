import functools


def count_calls(func):
    @functools.wraps( func )
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print( f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}" )
        return func( *args, **kwargs )

    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


# We need to add return statement:
def do_twice(func):
    def wrapper(a):
        func( a )
        func( a )

    return wrapper
