print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("Enter Player 1 choice: ")
print("***Don't look!***\n" * 30)
player2 = input("Enter Player 2 choice: ")

if player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("Player 2 wins!")
    elif player2 == "rock":
        print("Its a draw! Both players choose rock.")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print("Player 2 wins!")
    elif player2 == "paper":
        print("Its a draw! Both players choose paper.")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 wins!")
    elif player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print("Its a draw! Both players choose scissors.")
else:
    print("Something went wrong! Please type either rock, paper or scissors!")