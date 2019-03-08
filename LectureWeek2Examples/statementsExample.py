income = int(input("What is the taxable income? "))

if income <=18200:
    tax = 0
elif income <=37000:
    tax = (income - 18200)*0.19
elif income <= 90000:
    tax = 3572 + (income - 370000) * 0.325
else:
    tax = 20797 + (income - 90000)*0.037

print("Your tax is ", tax)