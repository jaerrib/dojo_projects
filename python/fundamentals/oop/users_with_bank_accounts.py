class BankAccount:

    all_accounts = []

    def __init__(self, int_rate=0.02, balance=0):
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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self, amount, other_user):
        self.make_deposit(amount)
        other_user.make_deposit(amount)


user1 = User("Joe Smith", "joesmith@email.com")
user1.make_deposit(100).make_deposit(200).make_deposit(150).make_withdrawal(125).display_user_balance()

user2 = User("Jane Smith", "janesmith@email.com")
user1.transfer_money(50, user2)
user2.display_user_balance()