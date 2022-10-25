#!/usr/bin/python3
"""
This is '0-read_file' module.
Functions and Classes:
    read_file(filename="")
"""


def read_file(filename=""):
    """read content of a file and print it to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
