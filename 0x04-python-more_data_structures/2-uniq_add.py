#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_add = 0
    for i in set(my_list):
        my_add += i
    return my_add
