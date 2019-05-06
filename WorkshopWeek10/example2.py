class Account:
    def __init__(self, accNo, bal):
        self.accNo = accNo
        self.balance = bal

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough money, cannot withdraw")

a1 = Account('123', 100)
a1.deposit(100)
a1.withdraw(300)
a1.withdraw(50)
print(a1.balance)

# a1.balance = 0
# print(a1.balance)