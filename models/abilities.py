class Abilities:
    def __init__(self, strength: int, dexterity: int, constitution: int,
                 intelligence: int, wisdom: int, charisma: int) -> None:
        self.__strength = strength
        self.__dexterity = dexterity
        self.__constitution = constitution
        self.__intelligence = intelligence
        self.__wisdom = wisdom
        self.__charisma = charisma

    @property
    def strength_score(self) -> int:
        return self.__strength

    @property
    def strength_modifier(self) -> int:
        return self._calculate_modifier(self.__strength)

    @property
    def dexterity_score(self) -> int:
        return self.__dexterity

    @property
    def dexterity_modifier(self) -> int:
        return self._calculate_modifier(self.__dexterity)

    @property
    def constitution_score(self) -> int:
        return self.__constitution

    @property
    def constitution_modifier(self) -> int:
        return self._calculate_modifier(self.__constitution)

    @property
    def intelligence_score(self) -> int:
        return self.__intelligence

    @property
    def intelligence_modifier(self) -> int:
        return self._calculate_modifier(self.__intelligence)

    @property
    def wisdom_score(self) -> int:
        return self.__wisdom

    @property
    def wisdom_modifier(self) -> int:
        return self._calculate_modifier(self.__wisdom)

    @property
    def charisma_score(self) -> int:
        return self.__charisma

    @property
    def charisma_modifier(self) -> int:
        return self._calculate_modifier(self.__charisma)

    @staticmethod
    def _calculate_modifier(score: int) -> int:
        """
        Calculate the ability modifier based on the ability score.
        :param score: The ability score.
        :return: The ability modifier.
        """
        return (score - 10) // 2
