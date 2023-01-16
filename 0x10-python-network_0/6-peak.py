#!/usr/bin/python3
"""
This module contains a function to return peek of a list
"""


def find_peak(int_l):
    """
    finds a peak in a list of unsorted integers
    """
    if type(int_l) is list:
        for i in range(len(int_l)):
            is_peak = True
            if i-1 >= 0 and int_l[i-1] > int_l[i]:
                is_peak = False
            if i+1 < len(int_l) and int_l[i+1] > int_l[i]:
                is_peak = False
            if is_peak:
                return int_l[i]

    return None
