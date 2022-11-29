#!/usr/bin/python3
def print_last_digit(number):
    num_str = repr(number)
    ld = int(num_str[-1])
    print("{}".format(ld), end="")
    return ld
