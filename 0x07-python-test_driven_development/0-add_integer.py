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
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    result = a + b
    return result
