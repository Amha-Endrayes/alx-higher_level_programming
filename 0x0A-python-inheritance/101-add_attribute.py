#!/usr/bin/python3
""" If possible adds an attribute to an object
"""


def add_attribute(obj, name, value):
    """ Try to add an attribute to an object
    """
    if getattr(obj, '__dict__', None) is None:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
