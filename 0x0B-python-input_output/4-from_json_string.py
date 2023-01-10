#!/usr/bin/python3
"""Deserialise object"""

import json


def from_json_string(my_str):
    """Deserializes JSON str to object"""
    return json.loads(my_str)
