import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class D4(Die):
    def __init__(self):
        super().__init__(4)

class D6(Die):
    def __init__(self):
        super().__init__(6)

class D8(Die):
    def __init__(self):
        super().__init__(8)

