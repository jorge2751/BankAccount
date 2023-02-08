class BankAccount:
    
    all_accounts = []

    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        # add each new account to the list of accounts
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    
    def display_account_info(self):
        print("Balance:",self.balance)
        return self
    
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
            print("Interest Rate:", account.int_rate, "Balance:", account.balance)

user1 = BankAccount()
user2 = BankAccount()

user1.deposit(100).deposit(50).deposit(45).withdraw(80).yield_interest().display_account_info()
user2.deposit(100).deposit(150).withdraw(40).withdraw(50).withdraw(70).withdraw(100).yield_interest().display_account_info()
BankAccount.display_all_accounts()