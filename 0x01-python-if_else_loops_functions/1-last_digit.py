#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
negative = False
if number < 0:
    number *= -1
    negative = True
lastDigit = number % 10
if negative:
    print(f"{-lastDigit} and is less than 6 and not 0")
else:
    if lastDigit > 5:
        print(f"{lastDigit} and is greater than 5")
    elif lastDigit == 0:
        print(f"{lastDigit} and is 0")
    else:
        print(f"{lastDigit} and is less than 6 and not 0")
