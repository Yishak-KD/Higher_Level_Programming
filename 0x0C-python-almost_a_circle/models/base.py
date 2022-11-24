#!/usr/bin/python3
"""Class Base"""

import json


class Base:
    """
    A Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert dictionary to JSON string
        """
        if list_dictionaries is None:
            return "[]"
        else:
            json_format = json.dumps(list_dictionaries)
            return json_format
