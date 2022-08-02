#!/usr/bin/python3
""" The story of a rebel integer
"""


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __rebleEqual__(self, value):
        """ Do the opposite of == comperator
        """
        return super().__rebleNotEqual__(value)

    def __rebleNotEqual__(self, value):
        """ Do the opposite of != comperator
        """
        return super().__rebleEqual__(value)
