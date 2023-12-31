#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """Return sum of two integers

        Args:
            a (int) - First integer parameter
            b (int) - Second integer parameter

        Returns:
            Sum of two integer numbers

        Raises:
            TypeError - if either parameters is not an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
