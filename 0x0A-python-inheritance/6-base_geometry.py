#!/usr/bin/python3
""" Another template base class for geometric objects
"""


class BaseGeometry:
    """ Base class or geometric objects
    """
    def area(self):
        """ Calculate the area of a geometric object
        """
        raise Exception("area() is not implemented")
