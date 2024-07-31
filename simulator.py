from models.monster import Monster


class Simulator:
    def __init__(self, total_simulations: int, party_1: list[Monster], party_2: list[Monster]) -> None:
        self.current_round: int = 0
        self.simulation_count: int = 0
        self.total_simulations: int = total_simulations
        self.party_1: list[Monster] = party_1
        self.party_2: list[Monster] = party_2
        self.simulation_results: dict[str, int] = {
            "party_1_wins": 0,
            "party_2_wins": 0,
        }

    def reset(self):
        self.current_round = 0
        for monster in self.party_1:
            monster.reset()
        for monster in self.party_2:
            monster.reset()

    def set_initiative_order(self):
        initiative_order = self.party_1 + self.party_2
        for monster in initiative_order:
            monster.initiative = monster.roll_initiative()
        initiative_order.sort(key=lambda monster: monster.initiative, reverse=True)
        return initiative_order

    def simulate_combat_round(self):
        initiative_order = self.set_initiative_order()
        while True:
            for monster in initiative_order:
                if not monster.is_alive():
                    continue
                monster.choose_target(self.party_1, self.party_2)
                monster.attack()
                if self.all_dead(self.party_1) or self.all_dead(self.party_2):
                    break
            self.current_round += 1
            if self.all_dead(self.party_1) or self.all_dead(self.party_2):
                break

    def simulate_encounter(self):
        while self.simulation_count < self.total_simulations:
            print(f"Simulation {self.simulation_count + 1} of {self.total_simulations} Simulations", end="\r")
            self.simulate_combat_round()
            if self.all_dead(self.party_1):
                self.simulation_results["party_2_wins"] += 1
            elif self.all_dead(self.party_2):
                self.simulation_results["party_1_wins"] += 1
            self.reset()
            self.simulation_count += 1

    def calculate_perecentages(self):
        party_1_percentage = self.simulation_results["party_1_wins"] / self.simulation_count * 100
        party_2_percentage = self.simulation_results["party_2_wins"] / self.simulation_count * 100
        return party_1_percentage, party_2_percentage

    @staticmethod
    def all_dead(party):
        return not any(monster.is_alive() for monster in party)

    def run(self):
        self.simulate_encounter()
        print(self.simulation_results)
        perc_1 , perc_2 = self.calculate_perecentages()
        print(f"{format(perc_1, ".2f")}%, {format(perc_2, ".2f")}%")
