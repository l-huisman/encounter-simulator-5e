

from constants.armor_type import ArmorType


class Armor:
    def __init__(self, name: str, armor_type: ArmorType, armor_class: int, weight: float, strength_req: int | None = None, stealth_disadvantage: bool = False, equipped_shield: int = 0) -> None:
        self.name = name
        self.armor_type = armor_type
        self.armor_class = armor_class
        self.weight = weight
        self.strength_req = strength_req
        self.stealth_disadvantage = stealth_disadvantage
        self.equipped_shield = equipped_shield

    def __str__(self):
        return f"{self.name} ({self.armor_class})"
    
    def calculate_armor_class(self, dex_mod: int) -> int:
        ac = self.armor_class
        if self.armor_type == ArmorType.LIGHT_ARMOR:
            ac = self.armor_class + dex_mod
        elif self.armor_type == ArmorType.MEDIUM_ARMOR:
            # Medium armor has a max dex mod of 2
            if dex_mod > 2:
                ac = self.armor_class + 2
            else:
                ac = self.armor_class + dex_mod
        else:
            ac = self.armor_class

        return ac + self.equipped_shield