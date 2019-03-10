print("You win if you guess the magic number.")
n = int(input("Enter a number: "))
if n == 3:
    print("You win!")
    print("It is the first odd prime. Yay!")
else:
    if n == 7:
        print("Some people think so, but not me.")
    print("Better luck next time.")
    if n < 3:
        print("Try higher.")
    else:
        print("Try lower.")