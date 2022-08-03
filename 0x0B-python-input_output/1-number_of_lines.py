#!/usr/bin/python3
""" A module that reads a file and does stuff
"""


def number_of_lines(filename=""):
    """Takes filename as string and reads the number of lines
    """

    with open(filename, encoding="utf-8") as readFile:
        lines = 0
        while True:
            line = readFile.readline()
            if not line:
                break
            lines += 1
        return lines
