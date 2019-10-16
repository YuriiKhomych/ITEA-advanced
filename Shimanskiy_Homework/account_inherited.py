from account import Account
a = Account('ffgh', 2)
import copy


class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __bool__(self):
        return self.owner

    def __setattr__(self, owner, amount):
        print(owner, amount)
        self.__dict__[owner] = amount

    def __getattr__(self, key):
        return self.__dict__[key]

    def __abs__(self):
        return self.amount



acc = Account('bob', 10)

acc.add_transaction(20)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30)

all_transaction = copy.deepcopy(acc._transactions)


class Bank(Account):
# Bank.__mro__
    def __init__(self,name, age):
        self.name = name
        self.age = age
        super().__init__()
        self.balance = all_transaction.append(super().balance()*2)


class International:
    def __init__(self, country):
        self.country = country


class BankSystem(Bank, International):
    def __init__(self, exist=None):
        self.exist = exist

BankSystem.__mro__
