from models.abilities import Abilities


class Character:
    def __init__(self, name: str, race: str, type: str, ability_scores: Abilities) -> None:
        self.name = name
        self.race = race
        self.type = type
        self.ability_scores = ability_scores

        def calculate_hit_points(self) -> int:
            raise NotImplementedError()

        def calculate_armour_class(self) -> int:
            raise NotImplementedError()

        @property
        def get_initiative_modifier(self) -> int:
            raise NotImplementedError()
