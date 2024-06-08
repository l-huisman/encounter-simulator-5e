from models.dice import Dice


class Weapon:
    def __init__(self, name: str, dice: Dice, proficient: bool = False):
        self.name: str = name
        self.dice: Dice = dice
        self.proficient: bool = proficient

