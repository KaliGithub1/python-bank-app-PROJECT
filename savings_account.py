from account import Account

class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.withdrawal_limit = 50000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited N{amount} to Savings Account."
        return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return f"Cannot withdraw more than N{self.withdrawal_limit} at a time."
        elif amount <= self.balance:
            self.balance -= amount
            return f"Withdrew N{amount} from Savings Account."
        else:
            return "Insufficient funds in Savings Account."

    def get_balance(self):
        return self.balance
