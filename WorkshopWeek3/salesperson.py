hours = int(input("Enter the hours worked for the week: "))
hourlyRate = 30.25
normalRateHours = 37
maxNormalPay = 1119.25
overtime = 1.5


if hours <= 37:
    print("You earnt: $", hours * hourlyRate)
elif hours > 37:
    print("You earnt: $", (hours - normalRateHours) * hourlyRate * overtime + maxNormalPay)

print("Sales Bonus")
bonusRate = 3
bonus = int(input("Enter the amount of camera gear sold: "))

if bonus <= 3000:
    print("Sorry you didn't sell enough cameras this week")
elif bonus > 3000:
    print("You made a bonus of: $", (bonus * bonusRate)/100)