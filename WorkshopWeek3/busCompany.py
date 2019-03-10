#Problem: A rugby team has 15 players. A bus company has only big busses that can carry 38
#passengers. Write a program that the tournament organiser can use to calculate the number
#of big busses that should be hired.


#Rugby Team
T = 15

#Big busses can carry 38 passengers
B = 38

b = int(input("How many big busses? "))
print("Number of teams =", (B * b) // T)