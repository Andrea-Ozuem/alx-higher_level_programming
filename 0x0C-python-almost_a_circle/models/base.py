#!/usr/bin/python

import json

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
        
