#!/usr/bin/python3
""" A module that handles jsons
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON
    """

    return obj.__dict__
