# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# c = float(input("Input third number: "))
# if a > b:
#     if a < c:
#         median = a
#     elif b > c:
#         median = b
#     else:
#         median = c
# else:
#     if a > c:
#         median = a
#     elif b < c:
#         median = b
#     else:
#         median = c
#
# print("The median is", median)

numberEntered = float(input("Enter a number: "))
numberEntered2 = 1
while numberEntered2 != 0:
    numberEntered2 = float(input("Enter a number: "))
    if numberEntered2 > numberEntered:
        median = numberEntered
    else:
        numberEntered = numberEntered
print("Median: '{}'" .format(median))