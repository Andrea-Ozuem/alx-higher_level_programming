#!/usr/bin/python3
""" Mylist Module"""


class MyList(list):
    """ A list"""

    def print_sorted(self):
        """Prints a list in sorted order"""
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
