#!/usr/bin/python3
"""
Imports add_0 module.
Prints the sum of two nummbers using this module.
Uses format string to display results.

"""
from add_0 import add

a = 1
b = 2

print ("{:d} + {:d} = {:d}\n".format(a,b, add(a,b))) 
