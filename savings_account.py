from account import Account 
class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
    def withdraw(self, amount, limit):
        if amount <= self.balance + limit:
            self.balance -= amount
        else:
            print("Withdrawal exceeds limit.")
    def __init__(self, balance=0):
        self.balance = balance
        self.withdrawal_limit = 50000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited N{amount} to Savings Account."
        return "SUCCESSFUL DEPOSIT."

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return f"Cannot withdraw more than N{self.withdrawal_limit} at a time."
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrew N{amount} from Savings Account.")
