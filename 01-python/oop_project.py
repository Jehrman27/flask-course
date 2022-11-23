####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self, name, balance):
        self.owner = name
        self.balance = balance

    def __repr__(self):
        return f"Account owner: {self.owner}\nBalance: {self.balance}"

    def deposit(self, depAmt):
        print(f"Depositing {depAmt} into the account")
        self.balance += depAmt
        print(self)

    def withdraw(self, withAmt):
        if withAmt <= self.balance:
            print(f"Withdrawing {withAmt} from the account")
            self.balance -= withAmt
            print(self)
        else:
            print(f"Sorry, insufficient funds to withdraw {withAmt}.")


# 1. Instantiate the class
acct1 = Account('Jose', 100)


# 2. Print the object
print(acct1)


# 3. Show the account owner attribute
acct1.owner


# 4. Show the account balance attribute
acct1.balance


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


acct1.withdraw(75)


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# ## Good job!
