#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """
        Attributes:
            width (int): width of the rect
            height (int): height of rect

        Class Attributes:
            number_of_instances (int): number of instances
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
                rect_str += str(self.print_symbol) * self.__width + "\n"

            return rect_str.rstrip()

    def __repr__(self):
        """Return a string representation of the rectangle for eval().

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete instance of object."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area
            Arguments:
                rect_1 (Rectangle): Instance of Rectangle
                rect_2 (Rectangle): Instance of Rectangle

            Raises:
                TypeError: rect_<number> must be an instance of Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
