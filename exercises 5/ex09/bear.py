"""File to define Bear class."""

class Bear:
    
    def __init__(self):
        self.age : int =  0
        self.hunger_score: int = 0
        self.hunger_score -= 1
        return None
    
    def one_day(self):
        self.age += 1
        return None
    
    def eat(self, num_fish: int ) -> None:
        self.hunger_score += num_fish
        return None