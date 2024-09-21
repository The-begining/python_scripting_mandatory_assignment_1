# Base Class: BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def account_info(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"

# Derived Class: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance is {self.balance}.")

# Derived Class: CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, transaction_fee=1):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    # Overriding the withdraw method to include transaction fee
    def withdraw(self, amount):
        total_withdrawal = amount + self.transaction_fee
        if self.balance >= total_withdrawal:
            self.balance -= total_withdrawal
            print(f"Withdrew {amount} (including {self.transaction_fee} fee). New balance is {self.balance}.")
        else:
            print("Insufficient funds to cover the withdrawal and transaction fee.")

# Test Cases
def test_bank_system():
    # Testing Standard BankAccount
    account1 = BankAccount("Shubham")
    print(account1.account_info()) 
    account1.deposit(500)
    account1.withdraw(200)
    print(account1.account_info())  # Expect balance to be 300

    # Testing SavingsAccount
    savings = SavingsAccount("Shubham_1", 1000)
    print(savings.account_info())  # Expect balance to be 1000
    savings.apply_interest()        # Applying 2% interest on balance
    print(savings.account_info())   # Expect increased balance after interest

    # Testing CheckingAccount
    checking = CheckingAccount("Shubham_2", 500)
    print(checking.account_info())  # Expect balance to be 500
    checking.withdraw(100)          # Withdraw 100 + 1 transaction fee
    print(checking.account_info())  # Expect balance to be 399


test_bank_system()