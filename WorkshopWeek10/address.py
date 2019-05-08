# file: address.py

"""A module that defines class Address."""


class Address:
    """An address."""

    def __init__(self, line1, line2, state, postcode):
        """Makes an address.

        For example: Address("5 Adelaide Avenue", "Deakin",
                             "ACT", "2600")"""
        self._line1 = line1
        self._line2 = line2
        self._state = state
        self._postcode = postcode

    def __str__(self):
        return self._line1 + "\n" + \
               self._line2 + "\n" + \
               self._state + " " + self._postcode