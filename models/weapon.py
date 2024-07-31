from constants.damage_type import DamageType
from constants.item_rarity import ItemRarity
from constants.weapon_property import WeaponProperty
from constants.weapon_type import WeaponType
from models.dice import Dice


class Weapon:
    def __init__(self, name, type: WeaponType, dice: Dice, damage_type: DamageType, 
                 rarity: ItemRarity, properties: list[WeaponProperty], range: tuple[int] | int, weight: float) -> None:
        self.name = name
        self.type = type
        self.dice = dice
        self.damage_type = damage_type
        self.rarity = rarity
        self.properties = properties
        self.range = range
        self.weight = weight

    def use(self):
        return self.dice.roll()
        

    