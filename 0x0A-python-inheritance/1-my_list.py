#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """
        Args:
            list (class) - Base class

        Attributes:
            print_sorted(self) - Function that prints sorted list(ascending order)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """Print list in sorted order(ascending order)"""
        sorted_list = sorted(self)
        print(sorted_list)
