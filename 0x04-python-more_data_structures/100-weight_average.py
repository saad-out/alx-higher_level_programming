#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0

    # Compute average
    if my_list:
        weights = 0
        for t in my_list:
            average += t[0]*t[1]
            weights += t[1]
        average /= weights

    return average
