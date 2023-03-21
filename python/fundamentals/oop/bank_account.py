class BankAccount:

    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            cls.display_account_info(account)


account1 = BankAccount(.03)
account2 = BankAccount(.04)

account1.deposit(100).deposit(200).deposit(50).withdraw(125).yield_interest()\
    .display_account_info()
account2.deposit(250).deposit(245.75).withdraw(20).withdraw(14.99).\
    withdraw(10.50).withdraw(75.98).yield_interest().display_account_info()
BankAccount.all_balances()
