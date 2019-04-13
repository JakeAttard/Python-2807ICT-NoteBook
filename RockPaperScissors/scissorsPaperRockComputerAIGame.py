import random

print("Welcome to scissors, paper, rock!")
print("To play please enter either scissors, paper or rock")

randomNumber = random.randint(0, 2)

if randomNumber == 0:
    computerAI = "scissors"
elif randomNumber == 1:
    computerAI = "paper"
else:
    computerAI = "rock"

player = input("Enter your choice: ")
print("Computer AI Turn: ", computerAI)

if player == "rock":
    if computerAI == "scissors":
        print("Player wins!")
    elif computerAI == "paper":
        print("Computer AI wins!")
    elif computerAI == "rock":
        print("Its a draw!")
elif player == "paper":
    if computerAI == "rock":
        print("Player wins!")
    elif computerAI == "scissors":
        print("Computer AI wins!")
    elif computerAI == "paper":
        print("Its a draw!")
elif player == "scissors":
    if computerAI == "rock":
        print("Computer AI wins!")
    elif computerAI == "paper":
        print("Player wins!")
    elif computerAI == "scissors":
        print("Its a draw!")
else:
    print("Something went wrong! Please type either rock, paper or scissors!")