#!/usr/bin/python3
""" A module that handles jsons and objects
"""
import json


def load_from_json_file(filename):
    """ Returns created object from a JSON file
    """

    with open(filename, mode="r", encoding="UTF-8") as readFile:
       return json.load(readFile) 
