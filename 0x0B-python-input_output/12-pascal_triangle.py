#!/usr/bin/python3
""" A module that returns a pascal trangel
"""


def pascal_triangle(n):
    """ Implmetation of a pascal triangle, takes an int as input
    Return a pascal triangl.
    """
    if n <= 0:
        return []

    resultTriangle = []
    for element in range(n):
        if element == 0:
            resultTriangle.append([1])
            continue
        if element == 1:
            resultTriangle.append([1, 1])
            continue
        row = []
        # init row
        for item in range(element + 1):
            row.append(item)
        for item in range(1, element):
            row[0] = 1
            row[element] = 1
            A = resultTriangle[element - 1][item]
            B = resultTriangle[element - 1][item - 1]
            row[item] = A + B
        resultTriangle.append(row)

    return resultTriangle
