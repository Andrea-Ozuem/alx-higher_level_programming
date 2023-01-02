#!/usr/bin/python3
""" Create C Rectangle Class"""


class Rectangle:
    """ Creates class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __str__(self):
        ret = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            [ret.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                ret.append("\n")
        return "".join(ret)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
