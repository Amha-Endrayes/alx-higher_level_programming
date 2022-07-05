#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for index in my_list:
        result.append(True if not index % 2 else False)
    return result
