#!/usr/bin/python3
"""Location for the python interpreter"""

class Square:
    """A class of square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing the class attributes
        :param size: Size parameter.
        :param position: Position of the tuple (x, y).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter property for the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter property for the size parameter."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter property for the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter property for the position tuple."""
        if type(value) != tuple or value[0] > 0 or value[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints with perimeter with #."""
        if self.__size == 0:
            print("")

        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
