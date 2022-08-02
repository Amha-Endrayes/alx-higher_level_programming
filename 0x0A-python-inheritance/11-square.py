#!/usr/bin/python3
""" A class for squares
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a Square of a fixed size
    """
    def __init_(self, size):
        """ initiates a square
        """
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be grater than 0")
        self.__size = size

    def __str__(self):
        """ Renders a square represented by a string
        """
        return '[Square] {size}/{size}'.format(size=self.__size)
