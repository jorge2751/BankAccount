class BankAccount:
    
    all_accounts = []

    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.account_number = len(BankAccount.all_accounts) + 1
        # add each new account to the list of accounts
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    
    def display_balance(self):
        print("Balance:",self.balance)
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        else:
            print("Can not earn interest on 0 balance")
        return self

    @classmethod
    def display_all_accounts(cls):
    # loop through all accounts and display their info
        for account in cls.all_accounts:
            print("Account Number:", account.account_number, "Interest Rate:", account.int_rate, "Balance:", account.balance)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
        self.create_account()
    
    def create_account(self):
        new_account = BankAccount(int_rate=0.02, balance=0)
        self.accounts.append(new_account)
        return self

    def select_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None
        
    def make_deposit(self, amount, account_number):
        account = self.select_account(account_number)
        if account:
            account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount, account_number):
        account = self.select_account(account_number)
        if account:
            account.withdraw(amount)
        return self

    def display_user_balance(self, account_number):
        account = self.select_account(account_number)
        if account:
            account.display_balance()
        return self



user1 = BankAccount()
user2 = BankAccount()

user1.deposit(100).deposit(50).deposit(45).withdraw(80).yield_interest().display_balance()
user2.deposit(100).deposit(150).withdraw(40).withdraw(50).withdraw(70).withdraw(100).yield_interest().display_balance()
BankAccount.display_all_accounts()


user3 = User("Jorge","jorge@gmail.com")

user3.make_deposit(300,3).make_withdrawal(80,3).display_user_balance(3)
user3.create_account().make_deposit(300,4).make_withdrawal(200,4).display_user_balance(4)
