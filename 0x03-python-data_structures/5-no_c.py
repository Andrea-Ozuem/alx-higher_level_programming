#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for char in my_string:
        if char in "cC":
            continue
        n_str += char
    return n_str
