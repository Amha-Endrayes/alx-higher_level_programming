#!/usr/bin/python3
""" Checks an objects inhertitance
"""


def inherits_from(obj, a_class):
    """ Checks if an object is an instance of an inherted class (subclass)
    """
    return isinstance(obj, a_class) and type(obj) != a_class
