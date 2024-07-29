from enum import Enum
from models.Abilities import Ability
from models.dice import Dice


def calculate_ability_modifier(ability: int) -> int:
    return (ability - 10) // 2


class ChallengeRating(Enum):
    """
    The challenge rating of a monster.

    :param challenge_rating: The challenge rating of the monster.
    :param experience_points: The experience points awarded for defeating the monster.
    :param proficiency_bonus: The proficiency bonus awarded for defeating the monster.
    """
    CR_0 = (0, 10, 2)
    CR_1_8 = (0.125, 25, 2)
    CR_1_4 = (0.25, 50, 2)
    CR_1_2 = (0.5, 100, 2)
    CR_1 = (1, 200, 2)
    CR_2 = (2, 450, 2)
    CR_3 = (3, 700, 2)
    CR_4 = (4, 1100, 2)
    CR_5 = (5, 1800, 3)
    CR_6 = (6, 2300, 3)
    CR_7 = (7, 2900, 3)
    CR_8 = (8, 3900, 3)
    CR_9 = (9, 5000, 4)
    CR_10 = (10, 5900, 4)
    CR_11 = (11, 7200, 4)
    CR_12 = (12, 8400, 4)
    CR_13 = (13, 10000, 5)
    CR_14 = (14, 11500, 5)
    CR_15 = (15, 13000, 5)
    CR_16 = (16, 15000, 5)
    CR_17 = (17, 18000, 6)
    CR_18 = (18, 20000, 6)
    CR_19 = (19, 22000, 6)
    CR_20 = (20, 25000, 6)
    CR_21 = (21, 33000, 7)
    CR_22 = (22, 41000, 7)
    CR_23 = (23, 50000, 7)
    CR_24 = (24, 62000, 7)
    CR_25 = (25, 75000, 8)
    CR_26 = (26, 90000, 8)
    CR_27 = (27, 105000, 8)
    CR_28 = (28, 120000, 8)
    CR_29 = (29, 135000, 9)
    CR_30 = (30, 155000, 9)

    def __init__(self, challenge_rating, experience_points, proficiency_bonus):
        self._challenge_rating = challenge_rating
        self._experience_points = experience_points
        self._proficiency_bonus = proficiency_bonus

    @property
    def get_challenge_rating(self):
        return self._challenge_rating

    @property
    def get_experience_points(self):
        return self._experience_points

    @property
    def get_proficiency_bonus(self):
        return self._proficiency_bonus


class Monster:
    """
    A monster in the game.

    :param name: The name of the monster.
    :param size: The size of the monster.
    :param race: The type of the monster.
    :param sub_race: The subtype of the monster.
    :param alignment: The alignment of the monster.
    :param strength: The strength of the monster.
    :param dexterity: The dexterity of the monster.
    :param constitution: The constitution of the monster.
    :param intelligence: The intelligence of the monster.
    :param wisdom: The wisdom of the monster.
    :param charisma: The charisma of the monster.
    :param hit_dice: The size of the hit dice of the monster.
    :param armour_class: The armour class of the monster.
    :param speed: The speed of the monster.
    :param skills: The skills of the monster.
    :param senses: The senses of the monster.
    :param languages: The languages of the monster.
    :param challenge_rating: The challenge rating of the monster.
    :param damage_vulnerabilities: The damage vulnerabilities of the monster.
    :param damage_resistances: The damage resistances of the monster.
    :param damage_immunities: The damage immunities of the monster.
    :param condition_immunities: The condition immunities of the monster.
    :param special_abilities: The special abilities of the monster.
    :param actions: The actions of the monster.
    :param bonus_actions: The bonus actions of the monster.
    :param legendary_actions: The legendary actions of the monster.
    :param reactions: The reactions of the monster.
    """

    def __init__(self, name: str, size: str, race: str, sub_race: str, alignment: str, strength: int, dexterity: int,
                 constitution: int, intelligence: int, wisdom: int, charisma: int,
                 hit_dice: Dice, armour_class: int, speed: int, skills: dict, senses: dict,
                 languages: list, challenge_rating: ChallengeRating, damage_vulnerabilities: list,
                 damage_resistances: list, damage_immunities: list, condition_immunities: list, special_abilities: list,
                 actions: list, bonus_actions: list, legendary_actions: list, reactions: list) -> None:
        self.name: str = name
        self.size: str = size
        self.race: str = race
        self.sub_race: str = sub_race
        self.alignment: str = alignment

        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.intelligence: int = intelligence
        self.wisdom: int = wisdom
        self.charisma: int = charisma

        self.strength_modifier: int = calculate_ability_modifier(strength)
        self.dexterity_modifier: int = calculate_ability_modifier(dexterity)
        self.constitution_modifier: int = calculate_ability_modifier(constitution)
        self.intelligence_modifier: int = calculate_ability_modifier(intelligence)
        self.wisdom_modifier: int = calculate_ability_modifier(wisdom)
        self.charisma_modifier: int = calculate_ability_modifier(charisma)

        self.hit_dice: Dice = hit_dice
        self.hit_points: int = self.calculate_hit_points()
        self.armour_class: int = armour_class
        self.speed: int = speed

        self.skills: dict = skills
        self.senses: dict = senses
        self.languages: list = languages

        self.challenge_rating: ChallengeRating = challenge_rating.get_challenge_rating()
        self.experience_points: int = challenge_rating.get_experience_points()
        self.proficiency_bonus: int = challenge_rating.get_proficiency_bonus()

        self.damage_vulnerabilities: list = damage_vulnerabilities
        self.damage_resistances: list = damage_resistances
        self.damage_immunities: list = damage_immunities
        self.condition_immunities: list = condition_immunities
        self.conditions: list = []

        self.special_abilities: list = special_abilities
        self.actions: list = actions
        self.bonus_actions: list = bonus_actions
        self.legendary_actions: list = legendary_actions
        self.reactions: list = reactions

        self.dead: bool = False
        self.unconscious: bool = False
        self.death_saving_throw_successes: int = 0
        self.death_saving_throw_failures: int = 0

    def calculate_hit_points(self, average: bool = True) -> int:
        base_hp = self.hit_dice.average_roll() if average else self.hit_dice.roll()
        additional_hp = self.constitution_modifier * self.hit_dice.amount
        return base_hp + additional_hp

    def roll_saving_throw(self, dc: int, ability: Ability) -> bool:
        roll = Dice(1, 20).roll()
        match ability:
            case Ability.STRENGTH:
                modifier = self.strength
            case Ability.DEXTERITY:
                modifier = self.dexterity
            case Ability.CONSTITUTION:
                modifier = self.constitution
            case Ability.INTELLIGENCE:
                modifier = self.intelligence
            case Ability.WISDOM:
                modifier = self.wisdom
            case Ability.CHARISMA:
                modifier = self.charisma
            case _:
                raise ValueError(f"Invalid ability: {ability}")
        return roll + modifier >= dc

    def take_damage(self, damage: int, damage_type: str = None):
        if damage_type in self.damage_vulnerabilities:
            self.hit_points -= damage * 2
        elif damage_type in self.damage_resistances:
            self.hit_points -= damage // 2
        elif damage_type in self.damage_immunities:
            return  # No damage taken
        else:
            self.hit_points -= damage
        if self.hit_points <= 0:
            self.unconscious = True

    def apply_condition(self, status_effect: str, duration: int, repeat_save: bool, disadvantage_on_save: bool):
        self.conditions.append((status_effect, duration, repeat_save, disadvantage_on_save))


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
