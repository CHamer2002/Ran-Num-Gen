import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

# Die subclasses for different sided dice
class D4(Die):
    def __init__(self):
        super().__init__(4)

class D6(Die):
    def __init__(self):
        super().__init__(6)

class D8(Die):
    def __init__(self):
        super().__init__(8)

class D10(Die):
    def __init__(self):
        super().__init__(10)

class D12(Die):
    def __init__(self):
        super().__init__(12)

class D20(Die):
    def __init__(self):
        super().__init__(20)

# Multi rolling function
def roll_multiple_dice(num_dice, dice_type):
    dice = [dice_type() for _ in range(num_dice)]
    results = [die.roll() for die in dice]
    total = sum(results)
    return results, total

def main():
    num_dice = int(input("How many dice would you like to roll? "))
    die_type = input("What type of die would you like to roll? (D4, D6, D8, D10, D12, D20) ")

    if die_type == "D4":
        dice_type = D4
    elif die_type == "D6":
        dice_type = D6
    elif die_type == "D8":
        dice_type = D8
    elif die_type == "D10":
        dice_type = D10
    elif die_type == "D12":
        dice_type = D12
    elif die_type == "D20":
        dice_type = D20
    else:
        print("Invalid die type. Defaulting to D6")
        dice_type = D6

    results, total = roll_multiple_dice(num_dice, dice_type)
    print(f"\nYou rolled {num_dice} {die_type} dice")

    for i, result in enumerate(results, 1):
        print(f"Die {i}: {result}")

    print(f"\nTotal: {total}")

if __name__ == "__main__":
    main()