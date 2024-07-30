import random
from models.abilities import Ability
from models.dice import Dice
from models.challenge_rating import ChallengeRating
from models.action import Action


def calculate_ability_modifier(ability: int) -> int:
    return (ability - 10) // 2


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

        self.challenge_rating: ChallengeRating = challenge_rating
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
        self.target = None

        self.dead: bool = False
        self.unconscious: bool = False
        self.death_saving_throw_successes: int = 0
        self.death_saving_throw_failures: int = 0

    def reset(self) -> None:
        self.hit_points = self.calculate_hit_points()
        self.target = None
        self.dead = False
        self.unconscious = False
        self.death_saving_throw_successes = 0
        self.death_saving_throw_failures = 0

    def choose_target(self, enemies: list["Monster"], party: list["Monster"]) -> "Monster":
        if self.target and random.random() < 0.75:
            return self.target

        if self in enemies:
            self.target = random.choice(party)
        else:
            self.target = random.choice(enemies)

    def is_alive(self) -> bool:
        return self.hit_points > 0 and self.death_saving_throw_failures < 3

    def roll_death_saving_throw(self) -> None:
        roll = Dice(1, 20).roll()

        if roll == 20:
            self.hit_points = 1
        elif roll == 1:
            self.death_saving_throw_failures += 2
        elif roll <= 9:
            self.death_saving_throw_failures += 1
        else:
            self.death_saving_throw_successes += 1

    def calculate_hit_points(self, average: bool = True) -> int:
        base_hp = self.hit_dice.average_roll() if average else self.hit_dice.roll()
        additional_hp = self.constitution_modifier * self.hit_dice.amount
        return base_hp + additional_hp

    def attack(self) -> None:
        if self.target and not self.target == self:
            for action in self.actions:
                if action.roll_to_hit() >= self.target.armour_class:
                    damage = action.roll_damage()
                    self.target.take_damage(damage)
                    action.apply_effects(self.target)

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
            self.hit_points = 0
            self.unconscious = True

    def apply_condition(self, status_effect: str, duration: int, repeat_save: bool, disadvantage_on_save: bool):
        self.conditions.append((status_effect, duration, repeat_save, disadvantage_on_save))

    def roll_initiative(self) -> int:
        return Dice(1, 20).roll() + self.dexterity_modifier
