#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
#    if len(tuple_a) < 2:
#       tuple_a = a[0], 0
    result = tuple(map(sum, zip(tuple_a, tuple_b)))
    return result
