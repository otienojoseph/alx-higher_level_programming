#!/usr/bin/python3
"""Square class"""


class Square:
    """Class to represent a Square"""

    def __init__(self, size=0):
        """
        Initialize Square class with length 'size'

        Args:
            size(int) - length/width of each side of the square

        Methods:
            area(self) - Returns area of square

            @property
            size(self) - Retrieve the size of square

            @size.setter
            size(self, value) - Set the size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns area of square based on size"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method that sets size with passed parameter value

        Args:
            value (int) - value to set size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
