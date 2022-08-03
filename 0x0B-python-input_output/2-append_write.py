#!/usr/bin/python3
""" A module that reads file and writes stuff
"""


def append_write(filename="", text=""):
    """Reads a file, writes a given string (appends) & returns length
    """

    with open(filename, mode="a", encoding="utf-8") as appendFile:
        appendFile.write(text)
        return len(text)
