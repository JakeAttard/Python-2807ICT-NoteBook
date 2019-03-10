print("You win if you guess the magic number.")
n = int(input("Enter a number: "))
if n == 3:
    print("You win!")
    print("It is the first odd prime. Yay!")
elif n == 7:
    print("Some people think so, but not me.")
    print("Try again")
else:
    print("Sorry.")
    print("Better luck next time.")