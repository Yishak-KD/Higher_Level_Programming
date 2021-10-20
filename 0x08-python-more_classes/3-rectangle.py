#!/usr/bin/python3
"""Location for the python interpreter"""

class Rectangle:
    """A class rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiating a class attribute
            Args:
                width: set the initial value of the width to 0
                height: set the initial value of the height to 0
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width"""
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height"""
        if type(self.__height) != int:
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
        return [2 * (self.width + self.height)]

    def __str__(self):
        """Print out using __str__"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
        return ""
