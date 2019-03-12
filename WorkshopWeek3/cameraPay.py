hours = int(input("Hours: "))
bonus = int(input("Sale: "))

wage = (hours * 30.25)

if hours <= 37:
    ow = 0
    print("Wage: $", wage)

else:
    hours > 37
    ow = (hours - 37) * 45.375
    print("Wage: $", (37 * 30.25) + ow)
    wage = (37 * 30.25 + ow)

if bonus <= 3000:
    b = 0
    print("Sorry you didn't sell enough cameras this week")
else:
    bonus > 3000
    b = (bonus-3000) * 0.03
    print("Bonus: $", b)

total = (wage + b)
print("Total: $", total)