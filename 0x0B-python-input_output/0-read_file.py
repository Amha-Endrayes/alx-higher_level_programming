#!/usr/bin/python3
""" A module that reads a file and does stuff
"""


def read_file(filename=""):
    """Takes in filename as string, reads and prints it
    """

    with open(filename, encoding="utf-8") as readFile:
        print(readFile.read(), end='')
