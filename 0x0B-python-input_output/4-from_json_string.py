#!/usr/bin/python3
""" A module that handles jsons and objects
"""
import json


def from_json_string(my_str):
    """ Returns a python object represented by a JSON string
    """

    return json.loads(my_str)
