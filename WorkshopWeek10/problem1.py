class Gocard:

    def __init__(self, bal):
        self.balance = bal
        self.transaction = [('initial balance', bal)]

    def topup(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction.append(('top up', amount))

    def ride(self, cost):
        if cost > 0:
            self.balance -= cost
            self.transaction.append(('ride', cost))

    def report(self):
        return self.balance

    def printTrans(self):
        b = self.transaction[0] [1]
        print('initial balance =', b)
        for t in self.transaction[1:]:
            if t[0] == 'topup':
                b = b + t[1]
            else:
                b = b - t[1]
            print(t[0], ' ', t[1], '', b)
        print("balance =", self.balance)

mycard = Gocard(100)
mycard.ride(3.5)
mycard.ride(5)
mycard.topup(20)
mycard.ride(5)
mycard.printTrans()

# def printCommand(vars, val):
#     if val.isalpha():
#         if val in vars:
#             print(val, 'equals', vars[val])
#         else:
#             print(val, 'is undefined.')
#     elif val.isdigit():
#         print(val)
#     else:
#         print("Syntax error.")

# Gocard = input("Creating account. Input initial balance: ")
#
# command = input("? ").strip()
# while command != 'q':
#     cs = command.split()
#     if len(cs) == 1 and cs[0] == 'b':
#         printTrans(Gocard.printTrans)
#     elif cs == 'r':
#         print()
#     elif cs == 't':
#         print()
#     else:
#         print("Bad Command.")
#     command = input("? ")
# print("Goodbye.")