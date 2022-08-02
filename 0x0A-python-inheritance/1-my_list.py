#!/usr/bin/python3
""" Sorts  a list of ints in ascending order
"""


class MyList(list):
    """ List manager
    """
    def print_sorted(self):
        """ Sorts and prints a list of numbers in ascending order
        """
        print(sorted(self))
