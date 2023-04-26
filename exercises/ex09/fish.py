"""File to define Fish class."""
__author__ = "730556908"


class Fish:
    """Class for Fish."""

    age: int
    
    def __init__(self):
        """Init method."""
        self.age = 0
        return None
    
    def one_day(self):
        """One_day method."""
        self.age += 1
        return None