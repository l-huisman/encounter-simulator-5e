from enum import Enum


class Abilities:
    def __init__(self, strength: int = 1, dexterity: int = 1, constitution: int = 1,
                 intelligence: int = 1, wisdom: int = 1, charisma: int = 1) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.abilityScoreModifiers = self._calculate_modifiers()

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


class Ability(Enum):
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"
