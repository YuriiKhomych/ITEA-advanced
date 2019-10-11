from magic_account import Account
import copy


class AccountInherited(Account):
    def __init__(self, owner, amount=0, bank_name=''):
        self.bankName = bank_name
        super().__init__(owner, amount)

    def bal(self):
        return super().balance

    def balance(self, mult):
        return self.amount * mult

    def get_owner(self):
        return self.owner, self.amount


acc_inc = AccountInherited('Avakov', 50)
print(acc_inc.get_owner())
print(acc_inc.balance(25))
print(acc_inc.bal())

print(AccountInherited.__mro__)

acc_incsc = copy.copy(acc_inc)
acc_incdc = copy.deepcopy(acc_inc)

acc_inc.add_transaction(30)

print(acc_inc.bal())
print(acc_incdc.bal())
print(acc_incdc.bal())





