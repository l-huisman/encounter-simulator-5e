import random
from abilities import Ability
from dice import Dice
from challenge_rating import ChallengeRating
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


monster_1 = Monster(
    name="Goblin",
    size="Small",
    race="Goblinoid",
    sub_race="",
    alignment="Neutral Evil",
    strength=8,
    dexterity=14,
    constitution=10,
    intelligence=10,
    wisdom=8,
    charisma=8,
    hit_dice=Dice(2, 6),
    armour_class=15,
    speed=30,
    skills={},
    senses={"darkvision": 60},
    languages=["Common", "Goblin"],
    challenge_rating=ChallengeRating.CR_1_4,
    damage_vulnerabilities=[],
    damage_resistances=[],
    damage_immunities=[],
    condition_immunities=[],
    special_abilities=[],
    actions=[Action("Scimitar", 2, 0, Dice(1, 6))],
    bonus_actions=[],
    legendary_actions=[],
    reactions=[]
)

monster_2 = Monster(
    name="Zombie",
    size="Medium",
    race="Undead",
    sub_race="",
    alignment="Neutral Evil",
    strength=13,
    dexterity=6,
    constitution=16,
    intelligence=3,
    wisdom=6,
    charisma=5,
    hit_dice=Dice(3, 8),
    armour_class=8,
    speed=20,
    skills={},
    senses={"darkvision": 60},
    languages=["Common"],
    challenge_rating=ChallengeRating.CR_1_4,
    damage_vulnerabilities=["bludgeoning"],
    damage_resistances=["piercing", "slashing"],
    damage_immunities=["poison"],
    condition_immunities=["poisoned"],
    special_abilities=[],
    actions=[Action("Slam", 2, 1, Dice(1, 6))],
    bonus_actions=[],
    legendary_actions=[],
    reactions=[]
)

initiative_order = []
initiative_dice = Dice(1, 20)

simulations = 1000
current_simulation = 0

goblin_results = {"encounters_won": 0, "encounters_lost": 0, "remaining_hit_points": 0, "initiative": 0}
Zombie_results = {"encounters_won": 0, "encounters_lost": 0, "remaining_hit_points": 0, "initiative": 0}

while current_simulation < simulations:
    monster_1 = monster_1
    monster_2 = monster_2

    monster_1.reset()
    monster_2.reset()

    monster_1.initiative = initiative_dice.roll() + monster_1.dexterity_modifier
    monster_2.initiative = initiative_dice.roll() + monster_2.dexterity_modifier

    initiative_order = [monster_1, monster_2]
    initiative_order.sort(key=lambda x: x.initiative, reverse=True)

    round = 1

    while True:
        for creature in initiative_order:
            if not creature.is_alive():
                creature.roll_death_saving_throw()
                continue

            creature.choose_target([monster_2], [monster_1])
            creature.attack()

            if not monster_2.is_alive() or not monster_1.is_alive():
                break

        round += 1

        if not monster_2.is_alive() or not monster_1.is_alive():
            break

    current_simulation += 1

    if monster_1.is_alive():
        goblin_results["encounters_won"] += 1
        Zombie_results["encounters_lost"] += 1

    if monster_2.is_alive():
        Zombie_results["encounters_won"] += 1
        goblin_results["encounters_lost"] += 1

    goblin_results["remaining_hit_points"] += monster_1.hit_points
    Zombie_results["remaining_hit_points"] += monster_2.hit_points
    goblin_results["initiative"] += monster_1.initiative
    Zombie_results["initiative"] += monster_2.initiative

print(f"\nResults: Goblin vs Zombie")
print(f"Percentage of Encounters Won: {goblin_results['encounters_won'] / simulations * 100}%")
print(f"Percentage of Encounters Lost: {Zombie_results['encounters_won'] / simulations * 100}%")
print(f"Average Remaining Hit Points Goblin: {goblin_results['remaining_hit_points'] / simulations}")
print(f"Average Remaining Hit Points Zombie: {Zombie_results['remaining_hit_points'] / simulations}")
print(f"Average Initiative Goblin: {goblin_results['initiative'] / simulations}")
print(f"Average Initiative Zombie: {Zombie_results['initiative'] / simulations}")
