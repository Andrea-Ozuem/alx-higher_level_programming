#!/usr/bin/python3
"""Rectangle Class"""


from base import Base


class Rectangle(Base):
    """Rectangel Class specifiction"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise a new Base"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Sets heights of rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Sets x- pffset"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Sets y-offset"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        """Str representation of object"""
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                               self.x,
                                                               self.y,
                                                               self.width,
                                                               self.height)

    def area(self):
        """Return area of Rectancle"""
        return self.width * self.height

    def display(self):
        """Displays rectangle using width and height"""
        for k in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print()

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        att = ["id", "width", "height", "x", "y"]
        if args and len(args):
            i = 0
            for arg in args:
                setattr(self, att[i], arg)
                i += 1
        else:
            for k, v in kwargs.items():
                if k in att:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
