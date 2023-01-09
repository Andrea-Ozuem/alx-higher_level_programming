#!/usr/bin/python3
""" Create class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates Rectangle subclass"""
    def __init__(self, size):
        self.integer_validator("size", width)
        self.__size = size

    def area(self):
        """ Method that returns the area of the instance"""
        return self.__size ** 2
