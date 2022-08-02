#!/usr/bin/python3
""" A class for rectangles
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangel(BaseGeometry):
    """ Defination of a fixed-size rectangel
    """
    def __init__(self, width, height):
        """ inits a rectangle parmeters
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
