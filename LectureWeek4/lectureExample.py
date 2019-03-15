# counter = 0
# while (True):
# 	i = int(input())
# 	if (i < 0):
# 		break
# 	counter += 1
# print('you have entered', counter, 'non-negative numbers')

# # Continue Statement
# i = 1
# while (i <= 100):
#     i += 1
#     if ((i - 1) % 2 == 0):
#         continue
#     print(i, end='')

# # For Loops
# for N in [2, 3, 5, 7]:
#     print(N, end='')#print all on same line

# For Loop Exmaple
# for student in ['David', 'Luke', 'Bob']:
#     print('Hello', student)

# for i in range(10):
#     print(i, end='')
#prints out 0 1 2 3 4 5 6 7 8 9

#Continue statement and for

# for n in range(20):
#     # if the remainder of n / 2 is 0, skip the rest of the loop
#     if n % 2 == 0:
#         continue
#     print(n, end='')
# Prints out 1 3 5 7 9 11 13 15 17 19

# #Nested Loops
# for i in range(10):
#     for j in range(10 - i):
#         print('*', end="")
#     print("\n")
#
# #Prints out
# **********
#
# *********
#
# ********
#
# *******
#
# ******
#
# *****
#
# ****
#
# ***
#
# **
#
# *

# # Loops with an else block
# L = []
# nmax = 30
# for n in range(2, nmax):
#     for factor in L:
#         if n % factor == 0:
#             break
#         else: #no break
#             L.append(n)
#     print(L)
#
# #Prints out
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []
# []

#Sequence of numbers
# a,b=0,1
# print(a, b , a+b, end="")
# MAXNUM = 1000
# while a+b <=MAXNUM:
#     a, b =b, a+b
#     print(b, end='')
#Prints out 0 1 1123581321345589144233377610987

#Counting in a loop
# zork = 0
# print('Before', zork)
# for thing in [9, 41, 12, 3, 74, 15] :
#     zork = zork + 1
#     print(zork, thing)
# print('After', zork)
#
# #Prints
# Before 0
# 1 9
# 2 41
# 3 12
# 4 3
# 5 74
# 6 15
# After 6