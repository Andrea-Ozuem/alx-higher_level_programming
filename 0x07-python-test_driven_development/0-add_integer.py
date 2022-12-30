#!/usr/bin/python3
""" Add function

Example:
    >>> add_integer(1, 2)
    3
"""


def add_integer(a, b=98):
    """ Adds two ints together"""
    if a is None:
        raise TypeError("a must be an integer")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
