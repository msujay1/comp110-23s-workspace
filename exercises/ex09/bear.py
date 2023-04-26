"""File to define Bear class."""
__author__ = "730556908"


class Bear:
    """Class for Bears."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Init method."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One_day method."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Eat method."""
        self.hunger_score += num_fish
        return None