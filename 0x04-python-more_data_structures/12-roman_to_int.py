#!/usr/bin/python3
def roman_to_int(roman_string):

    # check if not empty and is sring #
    if (roman_string is None) or (isinstance(roman_string, str) is False):
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last = 4000
    n = 0
    for c in roman_string:
        number = romans[c]
        if last < number:
            n += number - last
            last = 4000
        else:
            if last != 4000:
                n += last
            last = number

    if last != 4000:
        n += last

    return n
