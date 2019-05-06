# intialBalance = 100
#
# print("Creating account. Input initial balance:", intialBalance)
#

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return '{} {}'.format(emp1.first, emp1.last)


emp1 = Employee('Jake', 'Attard', 2000)
emp2 = Employee('Max', 'Cummins', 1000)

emp1.fullName()
emp2.fullName()
print(Employee.fullName(emp1))

# print(emp1.email)
# print(emp2.email)

# print(emp1.fullName())

# print('{} {}'.format(emp1.first, emp1.last))

# print(emp1)
# print(emp2)

# emp1.first = 'Jake'
# emp1.last = 'Attard'
# emp1.email = 'jakeattard18@gmail.com'
# emp1.pay = 6000
#
# emp2.first = 'Max'
# emp2.last = 'Cums'
# emp2.email = 'max@maxy.com'
# emp2.pay = 700