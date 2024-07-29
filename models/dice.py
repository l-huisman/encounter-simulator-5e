import math
import random


class Dice:
    def __init__(self, amount: int, sides: int) -> None:
        self.amount = amount
        self.sides = sides

    def roll(self) -> int:
        return sum([random.randint(1, self.sides) for _ in range(self.amount)])

    def average_roll(self) -> int:
        return math.floor(self.amount * (self.sides + 1) / 2)
