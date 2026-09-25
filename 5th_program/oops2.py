class Account:
    def action(self):
        print("Account Operation")
class Savings(Account):
    def action(self):
        print("Savings Account")
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)
name = input("Enter name: ")
balance = int(input("Enter balance: "))
amount = int(input("Enter deposit amount: "))
b = Bank(name, balance)
u = Savings()
u.action()
b.deposit(amount)