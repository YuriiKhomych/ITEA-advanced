def div_a_b(a, b):
    return a / b


# exception
class ContextManagerException:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type == self.exc_type:
            print("Caught exception")
            return True


with ContextManagerException(ZeroDivisionError):
    div_a_b(10, 0)
