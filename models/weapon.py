from constants.damage_types import DamageType
from constants.item_rarities import ItemRarities
from constants.weapon_properties import WeaponProperties
from constants.weapon_type import WeaponType
from models.dice import Dice


class Weapon:
    def __init__(self, name, type: WeaponType, category: str, dice: Dice, damage_type: DamageType, 
                 rarity: ItemRarities, properties: WeaponProperties, range: tuple[int] | int, weight: float) -> None:
        self.name = name
        self.type = type
        self.category = category
        self.dice = dice
        self.damage_type = damage_type
        self.rarity = rarity
        self.properties = properties
        self.range = range
        self.weight = weight

    def use(self):
        return self.dice.roll()
        

    