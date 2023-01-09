#!/usr/bin/python3
""" Create class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates Rectangle subclass"""
    def __init__(self, size):
        self.integer_validator("size", width)
        self.__size = size

    def area(self):
        """ Method that returns the area of the instance"""
        return self.__size ** 2
