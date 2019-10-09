# example 1
def are_you_robot(func):
    def check(*args):
        print('Welcome!')
        func(*args)
        print('By!')
    return check


@are_you_robot
def chose_film(name=''):
    robot_check = input('Are you robot? Y/N: ').upper()
    if robot_check in 'Y':
        print('Go away!')
    else:
        if name == '':
            print('Please choose the film')
        else:
            print('Thank you for choosing our resource')
            print('Your film is:', name)


chose_film("Devil's advocate")


# example 2
class CreateConnection:
    def __init__(self, connection_exist):
        self.connection_exist = connection_exist

    def __call__(self):
        print('Open connection')
        self.connection_exist()
        print('Connection closed')


@CreateConnection
def connection_e():
    print("You don't have read permission")


connection_e()

