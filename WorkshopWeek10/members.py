#file: members.py
#This module defines the members of the university.

from person import *

class Member(Person):
    #A Member is a Person with an ID that letters can be written to.

    def __init__(self, name, address, id):
        #Makes a Member.
        #name is a Name.
        #address is an Address.
        #id is a uni ID.

        Person.__init__(self, name, address)
        self.id = id

    def __str__(self):
        return self.id + " " + self.name.fullName()

    def writeALetter(self, body):
        #Write a letter to this Member with the given body text
        print(self.name)
        print(self.address)
        print()
        print("Dear " + self.name.firstName(), end = ",\n\n")
        print(body)
        print("\nRegards,")
        print("your University.")

class Student(Member):
    # A Student is a Member that can be excluded.

    def exclude(self):
        #Write an exclusion letter.
        self.writeALetter("""Your grades are rubbish. You are forwith excluded. Pay your fees on the way out.""")

class Staff(Member):
    #A Staff is a Member that can be fired.

    def fire(self):
        #Write a termination letter.
        self.writeALetter("""You are fired. Hand in your keys on the way out.""")