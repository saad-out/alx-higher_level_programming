#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size:
        first_char = sentence[0]
    else:
        first_char = 'None'
    t = (size, first_char)
    return t
