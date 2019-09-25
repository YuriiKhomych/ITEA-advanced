from magic_account import Account
import copy



class AccountInherited(Account):
    def __init__(self, owner, amount=0, bankName=''):
        self.bankName = bankName
        super().__init__( owner, amount )


#face_area = super().area()  # super(Square, self).area()
    def bal(self):
        return super().balance

    def balance(self,mult):
        return self.amount *mult

    def getOwner(self):
        return self.owner, self.amount

accInc = AccountInherited('Avakov',50)
print(accInc.getOwner())
print(accInc.balance(25))
print(accInc.bal())

print(AccountInherited.__mro__)

accIncsc=copy.copy(accInc)
accIncdc=copy.deepcopy(accInc)

accInc.add_transaction(30)

print(accInc.bal())
print(accIncsc.bal())
print(accIncdc.bal())





