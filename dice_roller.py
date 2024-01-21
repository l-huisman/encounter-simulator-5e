import random


class DiceRoller:
    def __init__(self):
        pass

    def roll(self, num_dice, num_sides):
        result = 0
        for i in range(num_dice):
            result += random.randint(1, num_sides)
        return result

    def roll_with_modifier(self, num_dice, num_sides, modifier):
        return self.roll(num_dice, num_sides) + modifier
