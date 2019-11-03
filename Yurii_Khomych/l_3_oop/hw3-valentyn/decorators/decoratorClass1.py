class SquareDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # before function
        print("Your number letter is: ", args[0], ", and it should be: ", chr(96+args[0]))
        print("But our function is going wrong and return next...")
        result = self.function(args[0]+1, **kwargs)
        return result

        # adding decorator to the class


@SquareDecorator
def get_letter(n):
    return chr(96+n)


print("Getting letter by index: ", get_letter(2))
