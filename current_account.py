from account import Account

class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited N{amount} to Current Account."
        return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew N{amount} from Current Account."
        else:
            return "Insufficient funds in Current Account."

    def get_balance(self):
        return self.balance
