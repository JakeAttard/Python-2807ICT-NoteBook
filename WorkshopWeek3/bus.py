#Problem: A rugby team has 15 players. A bus company has only big busses that can carry 38
#passengers. Write a program that the tournament organiser can use to calculate the number
#of big busses that should be hired.


T = 15
B = 38

t = int(input("How many teams? "))

print("Number of buses is =", (T * t) // B+1)