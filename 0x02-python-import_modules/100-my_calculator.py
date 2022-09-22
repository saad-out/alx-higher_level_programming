#!/usr/bin/python3
from sys import argv, exit
import calculator_1

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
