#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return 'None'
    max_number = my_list[0]
    for n in range(1, size):
        if my_list[n] > max_number:
            max_number = my_list[n]
    return max_number
