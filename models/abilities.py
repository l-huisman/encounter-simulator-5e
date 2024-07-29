from enum import Enum


class Ability(Enum):
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"


class Abilities:
    def __init__(self, strength: int = 10, dexterity: int = 10, constitution: int = 10,
                 intelligence: int = 10, wisdom: int = 10, charisma: int = 10) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.ability_score_modifiers = self._calculate_modifiers()

    def _calculate_modifiers(self) -> dict:
        return {
            Ability.STRENGTH: self._calculate_modifier(self.strength),
            Ability.DEXTERITY: self._calculate_modifier(self.dexterity),
            Ability.CONSTITUTION: self._calculate_modifier(self.constitution),
            Ability.INTELLIGENCE: self._calculate_modifier(self.intelligence),
            Ability.WISDOM: self._calculate_modifier(self.wisdom),
            Ability.CHARISMA: self._calculate_modifier(self.charisma)
        }

    @staticmethod
    def _calculate_modifier(ability: int) -> int:
        return (ability - 10) // 2

    def get_ability_modifier(self, ability: Ability) -> int:
        return self.ability_score_modifiers[ability]
