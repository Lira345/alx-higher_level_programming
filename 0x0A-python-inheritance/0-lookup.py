#!/usr/bin/python3


def lookup(obj):
    """
        Returns the list of available attributes and methods.
        Args:
            obj (object): object.
    """
    return (dir(obj))