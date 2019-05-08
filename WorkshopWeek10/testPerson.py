# file: testPerson.py
# Test driver for person.py.

from name import *
from address import *
from person import *

def test(person):
   print(person)
   print(person.name.firstName())
   print(person.name.canonName())
   print(person.address)

andrew = Person(
   Name("Rock", "Andrew B.", "Dr"),
   Address("10 Fred Street", "Lower Grunge",
           "Kingsland", "9999"))
test(andrew)
shinji = Person(
   Name("Ikari", "Shinji", "Mr", famFirst = True),
   Address("1034/23 Suwaru Road", "New Tokyo",
           "Tokyo", "ABZX"))
test(shinji)
