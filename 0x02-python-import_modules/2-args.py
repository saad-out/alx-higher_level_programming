#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    n = len(argv)
    print("{} argument".format(n - 1), end="")
    if n == 1:
        print("s.")
    elif n == 2:
        print(":")
    else:
        print("s:")
    for i in range(1, n):
        print("{}: {}".format(i, argv[i]))
