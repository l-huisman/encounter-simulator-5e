from dice import Dice


class Action:
    def __init__(self, name: str, proficiency_modifier: int, ability_modifier: int, damage_dice: Dice):
        self.name: str = name
        self.hit_dice: Dice = Dice(1, 20)
        self.damage_dice: Dice = damage_dice
        self.damage_modifier: int = ability_modifier
        self.hit_modifier: int = proficiency_modifier + ability_modifier

    def roll_to_hit(self):
        return self.hit_dice.roll() + self.hit_modifier

    def roll_damage(self):
        return self.damage_dice.roll() + self.damage_modifier

    def roll_critical_damage(self):
        return self.damage_dice.roll() + self.damage_dice.roll() + self.damage_modifier
