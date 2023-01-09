#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Create class"""


class Rectangle(BaseGeometry):
    """Creates Rectangle subclass"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Str method"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
    
    def area(self):
        """ Method that returns the area of the instance"""
        return self.__width * self.__height
