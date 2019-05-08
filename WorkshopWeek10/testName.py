# file: testName.py
# Test driver for name1.py.

from name import *

def test(name):
   print(name)
   print(name.firstName())
   print(name.canonName())

andrew = Name("Rock", "Andrew B.", "Dr")
test(andrew)
shinji = Name("Ikari", "Shinji", "Mr", famFirst = True)
test(shinji)