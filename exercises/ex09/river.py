"""File to define River class."""
__author__ = "730556908"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class."""

    day: int
    bears: list[Bear]
    fist: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals from a list."""
        new_bears: list[Bear] = list()
        new_fish: list[Fish] = list()
        for elem in self.bears:
            if elem.age <= 5:
                new_bears.append(elem)
        for elem in self.fish:
            if elem.age <= 3:
                new_fish.append(elem)
        self.bears = new_bears
        self.fish = new_fish
        return None

    def bears_eating(self):
        """Bears eating."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bears.eat(3)
        return None
    
    def check_hunger(self):
        """Checks hunger."""
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None
        
    def repopulate_fish(self):
        """Repopulates Fish."""
        return None
    
    def repopulate_bears(self):
        """Repopulates Bear."""
        return None
    
    def view_river(self):
        """Print the river status."""
        print(f'~~~ Day {self.day}: ~~~')
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calling one river week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes fish."""
        for i in range(amount):
            self.fish.pop(i)
        


            
