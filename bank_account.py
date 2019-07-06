class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.interest_rate = int_rate
        self.account_balance = balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        print("Balance: $", self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * self.interest_rate) 
        return self

baller = BankAccount(0.05, 25000)
not_a_baller = BankAccount()

# To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)

baller.deposit(10000).deposit(15000).deposit(30000).withdraw(25000).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)

not_a_baller.deposit(100).deposit(250).withdraw(40).withdraw(20).withdraw(130).withdraw(220).yield_interest().display_account_info()