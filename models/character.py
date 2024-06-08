from models import BaseClass
from models import Race


class Character:
    def __init__(self, race: Race, player_class: BaseClass) -> None:
        self.name: str = ""
        self.level: int = 1
        self.race: Race = race
        self.player_class: BaseClass = player_class
