#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str
    if n >= 0 and len(str) > n:
        new_str = new_str[0: n:] + new_str[n + 1::]
    return (new_str)
