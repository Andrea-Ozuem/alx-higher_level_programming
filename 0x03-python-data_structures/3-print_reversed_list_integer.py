#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list)
    for i in reversed(range(idx)):
        print("{:d}".format(my_list[i]))
        i -= 1
