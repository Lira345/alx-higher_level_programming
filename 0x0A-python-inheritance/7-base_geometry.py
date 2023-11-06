#!/usr/bin/python3
"""
    7-base_geometry: Class BaseGeometry
"""


class BaseGeometry:
    """
        baseGeometry
        attributes: None.
        methods:
            area() - raises an Exception
            integer_validator() - validates value.
    """
    def area(self):
        """
            area raise an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator checks the value of value.
            Args:
                name (str): name
                value (int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))