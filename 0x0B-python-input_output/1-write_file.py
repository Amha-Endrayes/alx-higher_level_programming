#!/usr/bin/python3
""" A module that reads file and writes stuff
"""


def write_file(filename="", text=""):
    """ Reads a file and writes a given string (overwrite)
    """

    with open(filename, mode="w", encoding="utf-8") as writeFile:
        writeFile.write(text)
        return len(text)
