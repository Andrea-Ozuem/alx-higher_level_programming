#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        num_str = ord(char)
        if num_str >= 97 and num_str <= 123:
            num_str-=32
        print("{}".format(chr(num_str)), end="")
    print()           
