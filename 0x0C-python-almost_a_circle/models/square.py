#!/usr/bin/python3


"""Square Class"""


from rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    Inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialse square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of class"""
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                       self.y, self.width)

    @property
    def size(self):
        """Sets size property"""
        return self.width

    @size.setter
    def size(self, size):
        """Ensures size is an int greater than 0"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates atrributes of object"""
        att = ["id", "size", "x", "y"]
        if len(args) != 0:
            i = 0
            try:
                for arg in args:
                    setattr(self, att[i], arg)
                    i += 1
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
