#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Overriding constructor from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set value to size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square with keyword-argument"""
        attributes = ['id', 'size', 'x', 'y']

        for idx, x in enumerate(args):
            if idx >= len(attributes):
                return

            self.__setattr__(attributes[idx], x)

        if args:
            return

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def to_dictionary(self):
        """Return dictionary representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
