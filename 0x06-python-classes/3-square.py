#!/usr/bin/python3
"""
Defines class Square
"""


class square:
    """ Defines optional private size attribute """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ returns area of the square """
    def area(self):
        return self.__size ** 2
