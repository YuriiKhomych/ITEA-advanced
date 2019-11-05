# example 1
def drink_beer(age):
    """Return approval or disapproval for drinking beer"""
    if age < 21:
        approval = False
        return approval


print(drink_beer.__doc__)


# example 2
def change_order():
    """Return value that was provided by user"""
    ideas = input('Please, share your ideas: ')
    return ideas


print(change_order.__doc__)

