class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}")
            return True
    def withdraw(self, amount):
        if self.acount_balance >= amount > 0:
            self.acount_balance -= amount
            print(f"Withdrew: ${amount}")
        elif amount <= self.account_balance:
            print("Insufficient funds.")

            return True
        return False
    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")