#!/usr/bin/python3
""" Creates square class"""


class Square:
    """ A square class"""
    def __init__(self, size=0):
        """Initialise sqaure instance

        Args:
            size: Size of square

        """
        self.__size = size

    @property
    def size(self):
        """Return size of self"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return Area of Square instance

        Returnl:
            area of square
        """
        return (self.__size)**2
