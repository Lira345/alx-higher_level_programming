#!/usr/bin/python3
"""
    2-append_write: append_write()
"""


def append_write(filename="", text=""):
    """
        Append_write appends a string at the end of a text file.
        Args:
            Filename (str): name of file
            Text (str): text to be appended to the file
        Returns: number of characters written
    """
    with open(filename, "a", encoding='utf=8') as a_file:
        return a_file.write(text)
