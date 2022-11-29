#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
num_str = num_str[-1]
if number < 0:
    num_str = "-" + num_str
ld = int(num_str)
print("Last digit of {} is".format(number), end=" ")
if ld > 5:
    print("{} and is greater than 5".format(ld))
elif ld == 0:
    print("{} and is 0".format(ld))
elif ld < 6 and ld != 0:
    print("{} and is less than 6 and not 0".format(ld))
