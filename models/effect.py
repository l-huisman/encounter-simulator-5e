from dice import Dice


class Effect:
    """
    An additional effect applied by an action.

    :param name: The name of the effect.
    :param saving_throw: The saving throw used to resist the effect.
    :param difficulty_class: The difficulty class of the saving throw.
    :param damage_dice: The dice used to calculate the damage of the effect.
    :param status_effect: The status effect applied by the effect.
    :param additional_damage_dice: Additional dice used to calculate the damage of the effect.
    :param half_damage_on_save: Whether the target takes half damage on a successful save.
    :param duration: The duration of the effect.
    :param repeat_save: Whether the target can repeat the saving throw.
    :param disadvantage_on_save: Whether the target has disadvantage on the saving throw.
     """

    def __init__(self, name: str, saving_throw: str = None, difficulty_class: int = 0, damage_dice: Dice = None,
                 status_effect: str = None, additional_damage_dice: Dice = None, half_damage_on_save: bool = False,
                 duration: int = 0, repeat_save: bool = False, disadvantage_on_save: bool = False):
        self.name: str = name
        self.saving_throw: str = saving_throw
        self.difficulty_class: int = difficulty_class
        self.damage_dice: Dice = damage_dice
        self.status_effect: str = status_effect
        self.additional_damage_dice: Dice = additional_damage_dice
        self.half_damage_on_save: bool = half_damage_on_save
        self.duration: int = duration
        self.repeat_save: bool = repeat_save
        self.disadvantage_on_save: bool = disadvantage_on_save

    def apply(self, target):
        saving_throw_result = target.roll_saving_throw(self.saving_throw)
        if not saving_throw_result < self.difficulty_class:
            if self.damage_dice:
                target.take_damage(self.damage_dice.roll())
            if self.status_effect:
                target.apply_status_effect(self.status_effect, self.duration, self.repeat_save,
                                           self.disadvantage_on_save)
            if self.additional_damage_dice:
                target.take_damage(self.additional_damage_dice.roll())
        else:
            if self.half_damage_on_save and self.additional_damage_dice:
                target.take_damage(self.additional_damage_dice.roll() // 2)
