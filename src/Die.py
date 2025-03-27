import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class D6(Die):
    def __init__(self):
        super().__init__(6)
