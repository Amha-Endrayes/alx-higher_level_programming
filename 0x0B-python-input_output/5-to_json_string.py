#!/usr/bin/python3
""" A module that handles jsons and objects
"""
import json

def to_json_string(my_obj):
    """ Return JSON format of my_obj
    """

    return json.dumps(my_obj)
