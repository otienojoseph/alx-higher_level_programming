#!/usr/bin/python3
"""Square class"""


class Square:
    """Class to represent a Square"""

    def __init__(self, size=0):
        """
        Initialize Square class with length 'size'

        Args:
            size(int) - length/width of each side of the square
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
