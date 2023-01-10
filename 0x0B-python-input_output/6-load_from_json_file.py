#!/usr/bin/python3
"""JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from acJSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
