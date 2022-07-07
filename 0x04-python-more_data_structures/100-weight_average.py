#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    resultant = 0.0
    scoreList = list(t[0] * t[1] for t in my_list)
    weightList = list(t[1] for t in my_list)
    resultant = sum(scoreList) / sum(weightList)
    return resultant
