#!/usr/bin/python3
"""A Sqaure class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=None)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
