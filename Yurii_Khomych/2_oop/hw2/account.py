from magic_account import Account


class AccountNew(Account):
    def __init__(self, owner, amount=0, bank_name=''):
        self.bankName = bank_name
        super().__init__(owner, amount)

    def __add__(self, other):
        if self.owner == other.owner:
            return AccountNew(self.owner, self.balance + other.balance, 'some_bank')

    def __sub__(self, other):
        print(self.owner, 'spent', other.balance)
        return AccountNew(self.owner, self.balance - other.balance, self.bankName)


acc = AccountNew('bob1', 10, 'ABC')
acc2 = AccountNew('bob13', 100, 'UBP')
print("", acc.balance)
print("", acc.owner)

try:
    acc3 = (acc + acc2)
    print('Owner {!r}, has {!r} in {!r}'.format(acc3.owner, acc3.balance, acc3.bankName))
except Exception:
    print("Owner is different!")


acc3 = (acc - acc2)
#print(acc3.balance)