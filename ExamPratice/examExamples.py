# for i in range(10):
#     for j in range(i):
#         print(i * j)


# x = 1
# y = -1
# z = 1
#
# if x > 0:
#     if y > 0:
#         print("x > 0 and y > 0")
# elif z > 0:
#     print("1 < 0 and 1 > 0")

# i = 1
# while i < 9:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i, end=' ')

# def nPrint(message, n):
#     while n > 0:
#         print(message)
#     n-= 1
# nPrint('a', 4)

# for i in range(10, 20):
#     for j in range(i):
#         print(i + j)

# i = 2
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 2

# def say(message, times = 1):
#     print(message * times)
# say('Hello')
# say('World', 3)

# n = int(input())
# for row in range(n):
#     for col in range(1, n - row + 1):
#         print(col, end=" ")
#     print()

# def nextSquare(n):
#     i = 0
#     while i * i <= n:
#         i += 1
#     return i * i

# for i in range(6):
#     for j in range(i):
#         print(j)

# for x in [1, 2, 4]:
#     for y in [4, 2, 1]:
#         if x != y:
#             if y < x:
#                 print("apple")
#             else:
#                 print("banana")
#         else:
#             print("cherry")

# print([(a, b) for a in "abc" for b in range(1, 3)])

# for i in range(8):
#     for j in range(16):
#         if (i + j) % 8 in [1, 5]:
#             print('/', end='')
#         elif (j - i) % 8 in [2, 6]:
#             print('\\', end='')
#         else:
#             print(' ', end='')
#     print()


# intList = [int(input()) for i in range(int(input()))]
# print(sum([intList[i] for i in range(len(intList))
#            if intList[i] not in intList[:i] + intList[i + 1:]]))

# def is_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True
# print(is_prime(1))

# import re
#
#
# def isValidPassword(password):
#     password = "jake"
#     flag = 0
#
#
# while True:
#     if (len(password) < 8):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]", password):
#         flag = -1
#         break
#     elif re.search("\s", password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
#
# if flag == -1:
#     print("Not a Valid Password")

# class Person:
#     def __init__(self, n, a):
#         self.fullName = n
#         self.age = a
#
#     def getAge(self):
#         return self.age
#
# class Student(Person):
#     def __init__(self, n, a, s):
#         Person.__init__(self, n, a)
#         self.school = s
#
#     def StudentSchool(self):
#         return self.school()

# class Person:
#     def __init__(self, name, dob, addr, income):
#         self.name = name
#         self.birthDate = dob
#         self.address = addr
#         self.income = income
#
#     def updateAddress(self, newAddress):
#         self.address = newAddress
#         print("Update Address " + self.address)
#
# p1 = Person("Jake Attard", "04-01-1999", "1 Griffith Drive GC", "$1,000")
# p1.updateAddress("Zac Cripps")

# def isValidPassword(word):
#     specialCharacters = ["#", "$", "%", "+"]
#     for i in word:
#         if i.isupper():
#             for j in word:
#                 if j.islower():
#                     for k in word:
#                         if k.isdigit():
#                             for a in word:
#                                 if a in specialCharacters:
#                                     return print("True")
#         else:
#             print("False")
#             break
# word = input()
# isValidPassword(word)

# i = 5
# while True:
#     if i % 9 == 0:
#         break
#     print(i, end="")
#     i += 1


# class Person:
#     def __init__(self, name, dob, addr, income):
#         self.name = name
#         self.birthDate = dob
#         self.address = addr
#         self.income = income
#
#     def printUserDetails(self):
#         print("Full Name: " + self.name)
#         print("Date Of Birth: " + self.birthDate)
#         print("Address: " + self.address)
#         print("Income: " + self.income)
#
# p1 = Person("David Smith", "23-Jan-2000", "28 Johnson Street, Southport QLD 4215", "$15308.5")
# p1.printUserDetails()

# for i in range(10, 20):
#     for j in range(i):
#         print(i + j)

# i = 2
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 2

def greaterCheck(list):
    for i in range(len(list)):
        if list[i][0] > list[i][1]:
            a = list[i][0]
            break
    return a
listA = [(10, 4), (5, 6), (1, 2)]
print(greaterCheck(listA))

def greaterChe2ck(list):
    orignalList = []
    for i in range(len(list)):
        if list[i][0] <= list[i][1]:
            orignalList.append(list[i])
    return orignalList
listA = [(1, 4), (8, 6), (1, 2)]
print(greaterCheck(listA))