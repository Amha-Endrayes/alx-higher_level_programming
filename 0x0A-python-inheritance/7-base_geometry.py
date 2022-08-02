#!/usr/bin/python3#!/usr/bin/python3
""" Another template base class for geometric objects
"""


class BaseGeometry:
    """ Base class or geometric objects
    """
    def area(self):
        """ Calculate the area of a geometric object
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Verifies if given dimensions are positive
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater that 0".format(name))
