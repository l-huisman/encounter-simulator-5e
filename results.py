class SimulationResults:
    def __init__(self) -> None:
        self.total_simulations: int = 0
        self.encounters_won: int = 0
        self.encounters_lost: int = 0
        self.surviving_enemies: list[int] = []
        self.surviving_adventurers: list[int] = []
        self.remaining_hit_points_enemies: list[int] = []
        self.remaining_hit_points_adventurers: list[int] = []
