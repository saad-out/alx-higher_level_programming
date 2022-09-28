#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for n in set(my_list):
        result += n
    return result
