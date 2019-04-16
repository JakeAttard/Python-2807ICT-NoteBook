import random

randomNumber = random.randint(1, 10)
player = None

while True:
    player = input("Pick a number from 1 to 10:")
    player = int(player)

    if player < randomNumber:
        print("The number you entered is to low!")
    elif player > randomNumber:
        print("The number you entered is to high!")
    else:
        print("You guess the number. You win!")
        playAgain = input("Do you want to play again? (y/n)")

        if playAgain == "y":
            randomNumber = random.randint(1, 10)
            player = None
        else:
            print("Thankyou for playing!")
            break