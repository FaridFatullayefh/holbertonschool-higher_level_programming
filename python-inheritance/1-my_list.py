#!/usr/bin/python3
"""
This module defines the MyList class.
"""


class MyList(list):
    """A subclass of list with custom sorting capabilities."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
