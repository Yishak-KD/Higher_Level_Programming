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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes to file with JSON string
        """
        with open(cls.__name__ + ".json", "w") as save_file:
            if list_objs is None:
                save_file.write("[]")
            """ #######"""

    @staticmethod
    def from_json_string(json_string):
        """Return list of json string representation
        """
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)
