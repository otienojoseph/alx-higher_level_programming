#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """
        Attributes:
            width (int): width of the rect
            height (int): height of rect
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Args:
                value (int): width value to set

            Raises:
                TypeError: if width is not an int
                ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return height of rect"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Args:
                value (int): width value to set

            Raises:
                TypeError: if width is not an int
                ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of rect"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of rect"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect_str = ""
            for i in range(self.__height):
                rect_str += "#" * self.__width + "\n"

            return rect_str.rstrip()
