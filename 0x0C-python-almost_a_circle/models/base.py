#!/usr/bin/python

import json
from os import path

"""Base Classs"""


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filenm = "{}.json".format(cls.__name__)
        with open(filenm, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                js_rep = [item.to_dictionary() for item in list_objs]
                f.write(cls.to_json_string(js_rep))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        elif cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if not path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
            js_str = f.read()
            ls_dic = cls.from_json_string(js_str)
            ls_instance = [cls.create(**att) for att in ls_dic]
            return ls_instance
