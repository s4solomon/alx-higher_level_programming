#!/usr/bin/python3
"""Module for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Rectangle class"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def integer_validator(var, condition):
        """Verify the type and value of an argument"""
        if type(var['value']) is not int:
            raise TypeError('{} must be an integer'
                            .format(var['name']))

        literal_condition = '{} {} 0'.format(var['value'], condition)
        if eval(literal_condition) is not True:
            raise ValueError('{} must be {} 0'
                             .format(var['name'], condition))

    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @property
    def x(self):
        """Get the value of x"""
        return self.__x

    @property
    def y(self):
        """Get the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set value to width"""
        Rectangle.integer_validator({'name': 'width', 'value': value}, '>')
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value to height"""
        Rectangle.integer_validator({'name': 'height', 'value': value}, '>')
        self.__height = value

    @x.setter
    def x(self, value):
        """Set value to x"""
        Rectangle.integer_validator({'name': 'x', 'value': value}, '>=')
        self.__x = value

    @y.setter
    def y(self, value):
        """Set value to y"""
        Rectangle.integer_validator({'name': 'y', 'value': value}, '>=')
        self.__y = value

    def area(self):
        """Calculates the area of a rectangle (w * h)"""
        return self.__width * self.__height

    def display(self):
        """Print a rectangle and # as pattern"""
        w, h = self.width, self.height
        x, y = self.x, self.y

        print('\n' * y, end='')
        pattern = '{}' \
            .format((' ' * x + '#' * w + '\n') * self.__height)
        print(pattern, end='')

    def __str__(self):
        """Overriding str method from Base"""
        return '[Rectangle] ({}) {}/{} - {}/{}' \
            .format(self.id, self.x, self.y, self.width, self.height)

    @staticmethod
    def generate_setter(name, value):
        """Return the setter in literal for do an evaluation"""
        setter = 'self.{} = {}'.format(name, value)
        return setter

    def update(self, *args, **kwargs):
        """Update the object with keyword-argument"""
        attributes = ['id', 'width', 'height', 'x', 'y']

        for idx, x in enumerate(args):
            if idx >= len(attributes):
                return

            self.__setattr__(attributes[idx], x)

        if args:
            return

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
