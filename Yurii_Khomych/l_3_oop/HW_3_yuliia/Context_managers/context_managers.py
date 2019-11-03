from contextlib import ContextDecorator


# example as a class
class Visa:
    def __init__(self, visa_type):
        self.visa_type = visa_type
        self.approval = False

    def __enter__(self):
        if self.visa_type is 'Tourism':
            self.approval = True
            return self.approval
        else:
            return self.approval

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Please wait your document')


with Visa('Tourism') as visa:
    print(visa)


# example as decorator
class GetVisa(ContextDecorator):
    def __enter__(self):
        print('Apply for visa')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Get your documents')
        return False


@GetVisa()
def apply_for_visa():
    print('Complete application and come to embassy')


apply_for_visa()







