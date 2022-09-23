#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp = (tuple_a, tuple_b)
    a = b = i = 0
    for t in tmp:
        for n in t:
            if i == 0:
                a += n
            elif i == 1:
                b += n
            else:
                break
            i += 1
        i = 0
    t = (a, b)
    return t
