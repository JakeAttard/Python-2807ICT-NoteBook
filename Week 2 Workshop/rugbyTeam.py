#Bus Passengers
T = 15
B = 38
S = 10

b = int(input("How many big busses? "))
s = int(input("How many small busses? "))
print("Number of teams =", (B * b + S * s) // T)