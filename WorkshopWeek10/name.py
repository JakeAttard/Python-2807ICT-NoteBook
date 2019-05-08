# file: name.py

"""A module that defines class Name."""


class Name:
    """A person's name."""

    def __init__(self, familyName, otherNames, title,
                 famFirst=False):
        """Makes a person's name.

        For example: Name("Trump", "Donald John", "Mr") or
        Name("Kim", "Jong-un", "Mr", famFirst = True)."""
        self._familyName = familyName
        self._otherNames = otherNames
        self._title = title
        self._famFirst = famFirst

    def fullName(self):
        """Return person's full name in preferred format."""
        if self._famFirst:
            return self._title + " " + self._familyName + \
                   " " + self._otherNames
        else:
            return self._title + " " + self._otherNames + \
                   " " + self._familyName

    def canonName(self):
        """Return person's full canonical name."""
        return self._familyName + ", " + self._otherNames \
               + ", " + self._title

    def firstName(self):
        """Return person's first other name."""
        others = self._otherNames.split()
        return others[0]

    def __str__(self):
        return self.fullName()
