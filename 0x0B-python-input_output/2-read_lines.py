#!/usr/bin/python3
"""A module that reads files and does stuff
"""
import os


def read_lines(filename="", nb_lines=0):
    """ Takes a files path, reads it and prints a set num of lines 
    """


    with open(filename, encoding="utf-8") as readFile:
        lineNum = 0
        while True:
            line = readFile.readline()
            lineNum += 1
            print(line, end='')
            if lineNum >= nb_lines and nb_lines > 0:
                break 
            if not line:
                break
