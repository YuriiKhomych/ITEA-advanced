from magic_account import Account


class NewAccount(Account):
    def __neg__(self):
        self.amount = self.amount*(-1)
        return self.amount

    def __copy__(self, new_owner):
        self.owner = new_owner.capitalize()
        return self.owner


a = NewAccount('Bob', 2)

a.add_transaction(2)
a.__neg__()
print(a)
a.__copy__('carmen')
print(a)
print(NewAccount.mro())



