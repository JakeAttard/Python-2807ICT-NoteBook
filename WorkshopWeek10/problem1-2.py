class Gocard:

    def __init__(self, bal):
        self.balance = bal
        self.transaction = [('Initial balance', bal)]

    def topup(self, amount):
        amount = float(amount)
        if amount > 0:
            self.balance += amount
            self.transaction.append(('Top up', amount))

    def ride(self, cost):
        cost = float(cost)
        if cost > 0:
            self.balance -= cost
            self.transaction.append(('Ride', cost))

    def report(self):
        print("Balance =", self.balance)

    def printTrans(self):
        b = self.transaction[0][1]
        print("Statement:")
        print("event", "    amount ($)  balance ($)")
        print('Initial balance', b)
        for t in self.transaction[1:]:
            if t[0] == 'Top up':
                b = b + t[1]
            else:
                b = b - t[1]
            print(t[0], ' ', t[1], '', b)
        print("Final Balance =", self.balance)

cardinput = int(input("Creating account. Input initial balance: "))
command = input("? ").strip()

mycard = Gocard(cardinput)

while command != 'q':
    commandsep = command.split()
    if len(commandsep) == 2 and commandsep[0] == 'r':
        mycard.ride(commandsep[1])
    elif len(commandsep) == 2 and commandsep[0] == 't':
        mycard.topup(commandsep[1])
    elif len(commandsep) == 1 and commandsep[0] == 'b':
        mycard.report()
    else:
        print("Bad command.")
    command = input("? ")
print(mycard.printTrans())