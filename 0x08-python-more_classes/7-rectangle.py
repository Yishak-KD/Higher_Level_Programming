#!/usr/bin/python3
"""Location for the python interpreter"""

class Rectangle:
    """A class of rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the class attributes
            Args:
                width: value of the width.
                height: value of the height.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Return a value from the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value using the setter property."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return a value from the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a value for the height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Function that returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return [2 * (self.__width + self.__height)]

    @property
    def __str__(self):
        """Prints out using __str__"""
        str_new = ""
        if self.__width == 0 or self.__height == 0:
            return str_new
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str_new += str(self.print_symbol)
                if i < self.__height:
                    str_new += "\n"
            return str_new

    def __repr__(self):
        """Special method used to represent a class's objects as a string."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Reserved function to delete object."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
