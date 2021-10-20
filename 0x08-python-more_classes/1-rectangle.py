#!/usr/bin/python3
"""Location for the python interpreter"""

class Rectangle:
    """A class of rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the class attributes
            Args:
                width: value of the width
                height: value of the height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return a value from the width"""
        return self.__width
    @width.setter
    def width(self, value):
        """Set a value property"""
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Return a value from the height"""
        return self.__height
    @height.setter
    def height(self, value):
        """Set a value for the height"""
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
