class Skills:
    def __init__(self):
        raise NotImplementedError()


class Skill:
    def __init__(self, name: str, ability: str, proficient: bool, expertise: bool):
        self.__name = name
        self.__ability = ability
        self.__proficient = proficient
        self.__expertise = expertise

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def proficient(self) -> bool:
        return self.__proficient

    @proficient.setter
    def proficient(self, proficient: bool) -> None:
        self.__proficient = proficient

    @property
    def expertise(self) -> bool:
        return self.__expertise

    @expertise.setter
    def expertise(self, has_expertise: bool) -> None:
        self.__expertise = has_expertise

    @property
    def ability(self) -> int:
        skill_modifier = self.__ability
        if self.__proficient:
            skill_modifier += proficiency_bonus
        if self.__expertise:
            skill_modifier += proficiency_bonus
        return skill_modifier
