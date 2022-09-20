#!/usr/bin/python3
def uppercase(str):
    for c in str:
        a = ord(c)
        if a >= 97 and a <= 122:
            a = chr(a - 32)
        else:
            a = c
        print("{}".format(a), end="")
    print("")
