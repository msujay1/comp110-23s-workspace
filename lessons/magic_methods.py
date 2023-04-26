from __future__ import annotations 

class Point:
    """Model a 2D Point"""

    x: float
    y: float
    
    def __init__(self, x: float, y: float):
        """Initialize a poitn with its x,y components"""
        self.x = x
        self.y = y

    def __str__(self):
        """Print prettier version of our point"""
        return f"({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled 
    
    def _add_(self, number: float) -> Point:
    
    
a: Point = Point(1.0, 2.0)
b: Point = a + 3.0
print(b)

