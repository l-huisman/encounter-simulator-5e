from action import Action
import random
import time

class Creature:
    def __init__(self, name: str, actions: list[Action], hit_points: int, armour_class: int, initiative_modifier: int) -> None:
        self.name = name
        self.initiative = 0
        self.actions = actions
        self.hit_points = hit_points
        self.armour_class = armour_class
        self.initiative_modifier = initiative_modifier

    def attack(self, target: "Creature") -> None:
        action = random.choice(self.actions)
        hit_roll = action.roll_to_hit()
        if hit_roll >= target.armour_class:
            damage = action.roll_damage()
            target.take_damage(damage)

    def take_damage(self, damage: int) -> int:
        self.hit_points -= damage

    def is_alive(self) -> bool:
        return self.hit_points > 0

    def set_initiative(self, initiative: int) -> None:
        self.initiative = initiative

    def get_initiative(self) -> int:
        return self.initiative
