class Account:
    # static attribute or class attributes or static variable
    minbal = 5000

    # static methods

    @staticmethod
    def getminbal():
        return Account.minbal

    def __init__(self, acno, ahname, bal=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount

    def getbalance(self):
        return self.balance


a1 = Account(1, "Scott", 20000)
a2 = Account(2, "Mark")
a1.deposit(10000)
a1.withdraw(5000)
print(a1.getbalance())

print(Account.getminbal())
