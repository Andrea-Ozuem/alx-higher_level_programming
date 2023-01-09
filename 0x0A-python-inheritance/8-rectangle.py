#!/usr/bin/python3
""" Create class"""


class BaseGeometry:
    """Create geometry calss"""
    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates values"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0") 

class Rectangle(BaseGeometry):
    """Creates Rectangle subclass"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
