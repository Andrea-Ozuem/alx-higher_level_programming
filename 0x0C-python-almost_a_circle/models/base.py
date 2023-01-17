#!/usr/bin/python

"""Base Classs"""


import json
from os import path


class Base:
    """Base Class
    This Represents the "base" for all other classes in project 0x0C*.
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise new base"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of inherited Base instances
        """
        filenm = "{}.json".format(cls.__name__)
        with open(filenm, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                js_rep = [item.to_dictionary() for item in list_objs]
                f.write(cls.to_json_string(js_rep))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                temp = cls(1, 1)
            elif cls.__name__ == "Square":
                temp = cls(1)
            temp.update(**dictionary)
            return temp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        if not path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
            js_str = f.read()
            ls_dic = cls.from_json_string(js_str)
            ls_instance = [cls.create(**att) for att in ls_dic]
            return ls_instance
