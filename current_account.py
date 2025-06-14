from account import Account
class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
CurrentAccount = CurrentAccount(200000) 
def deposit(self, amount):
    self.balance += amount
    return self.balance
def withdraw(self, amount):
    if amount > self.balance:
        print("Insufficient funds")
    self.balance -= amount
    return self.balance
CurrentAccount.withdraw(500)
def withdraw(self, amount):
    if amount > self.balance:
        print("Insufficient funds")
    self.balance -= amount
    return self.balance
def get_balance(self):
    return self.balance
CurrentAccount = Account(200000)

