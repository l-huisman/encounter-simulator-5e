from dice import Dice


class Action:
    """
    An action that a creature can take in combat.

    :param name: The name of the action.
    :param proficiency_modifier: The proficiency bonus of the creature.
    :param ability_modifier: The ability modifier of the creature.
    :param damage_dice: The dice used to calculate the damage of the action.
    :param effects: A list of effects that the action can apply.
    :param is_magical: Whether the action is magical or not.
    """

    def __init__(self, name: str, proficiency_modifier: int, ability_modifier: int, damage_dice: Dice = None,
                 effects: list = None, is_magical: bool = False):
        self.name: str = name
        self.hit_dice: Dice = Dice(1, 20) if damage_dice else None
        self.damage_dice: Dice = damage_dice
        self.damage_modifier: int = ability_modifier if damage_dice else 0
        self.hit_modifier: int = proficiency_modifier + ability_modifier if damage_dice else 0
        self.additional_effects: list = effects if effects else []
        self.is_magical: bool = is_magical

    def roll_to_hit(self) -> int:
        return self.hit_dice.roll() + self.hit_modifier if self.hit_dice else 0

    def roll_damage(self) -> int:
        return self.damage_dice.roll() + self.damage_modifier if self.damage_dice else 0

    def roll_critical_damage(self) -> int:
        return self.damage_dice.roll() + self.damage_dice.roll() + self.damage_modifier if self.damage_dice else 0

    def apply_effects(self, target):
        for effect in self.additional_effects:
            effect.apply(target)
