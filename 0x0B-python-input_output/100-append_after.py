#!/usr/bin/python3
""" A module that reads files and writes stuff
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a given string after another given string into filename
    """

    with open(filename, mode="r+", encoding="utf-8") as readFile:
        hold_My_Beer = readFile.readlines()

    count = 0
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        for lines in hold_My_Beer:
            count += 1
            if search_string in lines:
                hold_My_Beer.insert(count, new_string)
        for lines in hold_My_Beer:
            writeFile.write(lines)
