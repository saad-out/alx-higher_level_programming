#!/usr/bin/python3
"""
This is '2-append_write' module.
Functions and Classes:
    append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    append a string to a file and return number of characters read
    """
    with open(filename, "a", encoding="UTF-8") as f:
        nc = f.write(text)

    return nc
