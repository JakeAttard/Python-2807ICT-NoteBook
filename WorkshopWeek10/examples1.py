import random
class Coin:
    def __init__(self):
        self.sideup = "head"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "head"
        else:
            self.sideup = "tail"

    def show(self):
        print("This side is up:", self.sideup )

    def __str__(self):
        return self.sideup + " is the side up"

coin1 = Coin()
print(coin1)
coin1.toss()
coin1.show()
coin1.toss()
coin1.show()