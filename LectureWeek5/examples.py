# import math
#
# x = 10 / 3
# print("x = {:.4f}".format(x))
# print("ceil(x) = {:.4f}".format(math.ceil(x)))
# print("floor(x) = {:.4f}".format(math.floor(x)))

# def printBoo():
#     print("Boo!")
# printBoo()
# printBoo()
# printBoo()

# def printVertical(x):
#     """Print x vertically. """
#     for c in str(x):
#         print(c)
# printVertical("Boo!")
# printVertical(42)

# def finalBalance(p, r, n):
#     """Returns a final balance with compound interest:
#         p in the principle (initial balance)
#         r is the interest rate per term
#         n is the number of terms"""
#     return p * (1.0 + r) ** n
# initBal = float(input("Initial balance: "))
# annRatePct = float(input("Annual interest rate (%): "))
# months = int(input("Number on months: "))
# finalBal = finalBalance(initBal, annRatePct / 100.0 / 12.0, months)
# print("Final balance = ${:.2f}".format(finalBal))

# def printBox(width, height, empty = False, framed = False):
#     """Print a patterned box of size width x height characters."""
#     for i in range(height):
#         for j in range(width):
#             if framed and \
#                     (i == 0 and (j == 0 or j == width - 1) or \
#                      i == height - 1 and (j == 0 or j == width - 1)):
#                 print("+", end = "")
#             elif framed and (i == 0 or i == height - 1):
#                 print("-", end="")
#             elif framed and (j == 0 or j == width - 1):
#                 print("|", end="")
#             elif not empty and (i + j) % 2 == 0:
#                 print("X", end="")
#             elif not empty:
#                 print("0", end="")
#             else:
#                 print(" ", end="")
#         print()
# printBox(5, 3)
# printBox(10, 4, framed = True)
# printBox(10, 4, framed = True, empty = True)

# def f():
#     x = 2
#     print("a x =", x)
#     print("a x =", y)
# y = 1
# f()
# print("c y =", y)

# def f(x):
#     print("b x =", x)
#     x += 1
#     print("c x =", x)
# y = 1
# print("a y =", y)
# f(y)
# print("d y =", y)

# from math import sin, cos
# def polarToRect(r, theta):
#     """Convert the polar coordinates (r, theta (rad)) to rectangular coordinates (x, y)."""
#     return (r * cos(theta), r * sin(theta))


# pi = 3.14156
# print("the value of pi is {}".format(pi))
