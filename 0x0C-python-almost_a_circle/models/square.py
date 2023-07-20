#!/usr/bin/python3
"""Initiates square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Methods and parameters for square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Creates a new Square with parameters"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Defines the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square with parameters"""
        if args and len(args) != 0:
            t = 0
            for arg in args:
                if t == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif t == 1:
                    self.size = arg
                elif t == 2:
                    self.x = arg
                elif t == 3:
                    self.y = arg
                t += 1

        elif kwargs and len(kwargs) != 0:
            for q, j in kwargs.items():
                if q == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif q == "size":
                    self.size = j
                elif q == "x":
                    self.x = j
                elif q == "y":
                    self.y = j

    def to_dictionary(self):
        """Output dictionary representation of the Square."""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """Output print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
