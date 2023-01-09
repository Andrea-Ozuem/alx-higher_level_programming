#!/usr/bin/python3
""" Issubclass implementation Module"""


def inherits_from(obj, a_class):
    """Checks if obj is a subclass of a_class"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
