from constants.damage_type import DamageType
from constants.item_rarity import ItemRarity
from constants.weapon_property import WeaponProperty
from constants.weapon_type import WeaponType
from models.dice import Dice


class Weapon:
    def __init__(self, name, type: WeaponType, dice: Dice, damage_type: DamageType, rarity: ItemRarity, 
                 properties: list[WeaponProperty], range: tuple[int] | int, weight: float, 
                 extra_dmg_dice: Dice | None = None, extra_dmg_type: DamageType | None = None ,is_magic: bool = False
                 ) -> None:
        self.name = name
        self.type = type
        self.dice = dice
        self.damage_type = damage_type
        self.rarity = rarity
        self.properties = properties
        self.range = range
        self.weight = weight
        self.extra_dmg_dice = extra_dmg_dice
        self.extra_dmg_type = extra_dmg_type
        self.is_magic = is_magic
        

    