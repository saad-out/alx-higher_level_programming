#!/usr/bin/python3
"""
This module contains a function to return peek of a list
"""


def find_peak(int_l):
    """
    finds a peak in a list of unsorted integers
    """
    if not int_l or type(int_l) is not list:
        return None

    left, right = 0, len(int_l) - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid < len(int_l) and int_l[mid] < int_l[mid + 1]:
            left = mid + 1
        elif mid >= 0 and int_l[mid] < int_l[mid - 1]:
            right = mid - 1
        else:
            return int_l[mid]

    return left
