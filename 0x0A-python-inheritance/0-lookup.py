#!/usr/bin/python3
"""
    Lookup function that returns a list of avialable
    attributes and methods
"""


def lookup(obj):
    """
        Args:
            obj - Object
    """

    return dir(obj)
