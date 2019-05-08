#file: testMembers.py
#Test driver for members.py

from name import *
from address import *
from members import *

andrew = Staff(
    Name("Rock", "Andrew B.", "Dr"),
    Address("10 Fred Street", "Lower Grunge", "Kingsland", "9999"),
    "S1234567")
andrew.fire()
print("----------------")
jake = Student(
    Name("Attard", "Jake", "Mr", famFirst - True),
    Andress("1034/23 Suwari Road", "New Tokyo", "Tokyo", "ABZX"),
    "S7654321")
jake.exclude()