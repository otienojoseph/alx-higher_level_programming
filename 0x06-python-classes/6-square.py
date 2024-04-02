#!/usr/bin/python3
"""Square class"""


class Square:
    """Class that represent a Square

    Attributes:
        __size(int) - The size of each side of square object.
        __position(tuple, optional) - The position of a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize Square object with a given size and position

        Args:
            size(int, optional) - The size of each side of square object.
            Defaults to 0.
            position(tuple, optional) - The position of a square.
            Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter for the size attribute

        Return:
            int - size of each side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute

        Args:
            value (int) - size of each side of the square

        Raises:
            TypeError: If size not an int
            ValueError: If size less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ "
        Getter for the position attribute

        Return:
            tuple - position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute

        Args:
            value (tuple) - position of square

        Raises:
            TypeError: If position is not a tuple
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate the area of a square

        Return:
            int: Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints square using the '#' character
        """
        if self.__size == 0:
            print()

        try:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        except (TypeError, IndexError):
            print("position must be a tuple of 2 positive integers")
