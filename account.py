class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Amount withdrew {amount:.2f}. New balance: {self.balance:.2f}"
def deposit(self, amount):
    self.balance += amount
    return f"Amount deposited {amount:.2f}. New balance: {self.balance:.2f}" 
    if amount <= 1000:
        return "Deposit amount must be greater than 1000."
    else:
        self.balance += amount
        return f"Amount deposited {amount:.2f}. New balance: {self.balance:.2f}"
def get_balance(self, balance):
     self.balance= balance 
     return f"Current balance: {self.balance:.2f}"
