#!/usr/bin/python3
"""Square class"""


class Square:
    """Class to represent a Square"""

    def __init__(self, size):
        """
        Initialize Square class with length 'size'

        Args:
            size(int) - length/width of each side of the square
        """
        self.__size = size
