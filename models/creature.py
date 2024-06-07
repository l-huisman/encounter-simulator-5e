import random

from models.action import Action
from models.dice import Dice


class Creature:
    def __init__(self, name: str, actions: list[Action], hit_points: int, armour_class: int,
                 initiative_modifier: int) -> None:
        self.name: str = name
        self.initiative: int = 0
        self.actions: list[Action] = actions
        self.hit_points: int = hit_points
        self.armour_class: int = armour_class
        self.initiative_modifier: int = initiative_modifier
        self.target: Creature = None
        self.death_saves: int = 0
        self.death_fails: int = 0

    def attack(self) -> None:
        action = random.choice(self.actions)
        hit_roll = action.roll_to_hit()
        if hit_roll == 20:
            damage = action.roll_critical_damage()
            self.target.take_damage(damage)
        if hit_roll >= self.target.armour_class:
            damage = action.roll_damage()
            self.target.take_damage(damage)

    def choose_target(self, enemies: list["Creature"], party: list["Creature"]) -> "Creature":
        if self.target and random.random() < 0.75:  # 75% chance to keep the same target
            return self.target

        if self in enemies:
            self.target = random.choice(party)
        else:
            self.target = random.choice(enemies)

        return self.target

    def roll_death_saving_throw(self) -> None:
        roll = Dice(1, 20).roll()

        if roll == 20:
            self.hit_points = 1
        elif roll == 1:
            self.death_fails += 2
        elif roll <= 9:
            self.death_fails += 1
        else:
            self.death_saves += 1

    def take_damage(self, damage: int) -> None:
        self.hit_points -= damage

    def is_alive(self) -> bool:
        return self.hit_points > 0 and self.death_fails < 3

    def set_initiative(self, initiative: int) -> None:
        self.initiative = initiative

    def get_initiative(self) -> int:
        return self.initiative
