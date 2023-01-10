#!/usr/bin/python3
"""Function add_attribute"""


def add_attribute(a_class, name, value):
    """Adds new attribute to an object if it's possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
