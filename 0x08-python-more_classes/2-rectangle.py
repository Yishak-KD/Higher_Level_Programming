#!/usr/bin/pyhton3
"""Location of the python interpreter"""

class Rectangle:
    def __init__(self, width=0, height=0):
        """Instantiating
        Args:
            width: the width of rectangle
            height: the height of rectangle
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the property of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the property of the width"""
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the property of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the property of the setter"""
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function that returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """A function that returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return [2 * (self.__width + self.__height)]
