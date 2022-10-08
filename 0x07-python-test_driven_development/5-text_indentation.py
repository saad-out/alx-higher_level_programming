#!/usr/bin/python3
"""
This is '5-text_indentation' module.
Functions:
    text_indentation(text)
"""


def text_indentation(text):
    """
    text with 2 new lines after each of these characters: ., ? and :

    args:
        text (str): given text
    return:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    start = end = 0
    size = len(text)
    while end < size:
        while text[start] == ' ':
            start += 1
            end += 1
        while end < size and text[end] not in '.?:':
            end += 1
        # print("going to print {}, {}".format(start, end))
        print(text[start:end+1], end="")
        if end != size:
            print("\n")
        end += 1
        start = end
