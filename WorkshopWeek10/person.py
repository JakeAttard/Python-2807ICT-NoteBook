# file: person.py

"""A module that defines class Person."""

class Person:
    """A Person has a name and an address."""

    def __init__(self, name, address):
        """Makes a Person.

        name is a Name.
        address is an Address."""
        self.name = name
        self.address = address

    def __str__(self):
        return str(self.name)