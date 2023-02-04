# 从random模块中导入我们需要的randint函数
from random import randint


class Die:
    """A class representing a single die."""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        
    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
        # randint()
        # Return random integer in range [a, b], including both end points.
