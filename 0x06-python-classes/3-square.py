#!/usr/bin/python3
""" Creates square class"""


class Square:
    """ A square class"""
    def __init__(self, size=0):
        """Initialise sqaure instance

        Args:
            size: Size of square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return Area of Square instance

        Returnl:
            area of square
        """

        return (self.__size)**2
