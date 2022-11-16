#!/usr/bin/python3
"""A class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self):
        self.__y = y
