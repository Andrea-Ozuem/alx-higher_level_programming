#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_list = my_list.copy()
    n_list[idx] = element
    return n_list