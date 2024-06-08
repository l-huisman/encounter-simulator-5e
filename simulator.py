from models.action import Action
from models.creature import Creature
from models.dice import Dice
from results import SimulationResults


class Simulator:
    def __init__(self, total_simulations: int, adventurers_highest_damage: bool):
        self.round: int = 0
        self.simulation_count: int = 0
        self.initiative_dice: Dice = Dice(1, 20)
        self.total_simulations: int = total_simulations
        self.adventurers_highest_damage: float = adventurers_highest_damage
        self.simulation_results: SimulationResults = SimulationResults()
        self.party: list[Creature] = []
        self.enemies: list[Creature] = []

    def run(self, enemy_count):
        # Run the simulation until the simulation count
        while self.simulation_count < self.total_simulations:
            # Create the list of enemies
            self.enemies: list[Creature] = [Creature("Goblin", [Action("Scimitar", 2, 2, Dice(1, 6)), Action("Longbow", 2, 2, Dice(1, 8))], 7, 15, 2) for i in range(enemy_count)]

            # Create an adventuring party
            self.party: list[Creature] = [
                Creature("Fighter", [Action("Longsword", 2, 3, Dice(1, 8)), Action("Shortbow", 2, 2, Dice(1, 6))], 13,
                         18, 2),
                Creature("Rogue", [Action("Shortsword", 2, 3, Dice(1, 6)), Action("Shortbow", 2, 3, Dice(1, 6))], 11,
                         15, 3),
                Creature("Wizard", [Action("Firebolt", 2, 3, Dice(1, 10)), Action("Chill Touch", 2, 3, Dice(1, 8))], 9,
                         12, 1),
                Creature("Cleric", [Action("Mace", 2, 1, Dice(1, 6)), Action("Longbow", 2, 0, Dice(1, 8))], 10, 16, 0),
            ]

            if self.simulation_count % 10000 == 0:
                print(f"Simulation {self.simulation_count} of {self.total_simulations}", end="\r", flush=True)

            # Set initiative order
            initiative_order = self.set_initiative_order()

            # Set the round to 0
            self.round = 1

            # Simulate the combat round
            self.simulate_combat_rounds(initiative_order)

        # Print the results
        self.print_results()

    def simulate_combat_rounds(self, initiative_order: list[Creature]) -> None:
        # Encounter loop
        while True:
            # Iterate through the initiative order
            for creature in initiative_order:
                # If the creature is dead, skip their turn
                if not creature.is_alive():
                    creature.roll_death_saving_throw()
                    continue

                # If the creature is an enemy, attack a random adventurer
                if not creature.is_unconscious():
                    creature.choose_target(enemies, self.party)
                    creature.attack()

                # Check if all enemies or all adventurers are dead
                if self.all_enemies_dead(self.enemies) or self.all_adventurers_dead():
                    break

            # Increment the round
            self.round += 1

            # If all the enemies are dead, end the combat
            if not any(enemy.is_alive() for enemy in self.enemies) or not any(
                    adventurer.is_alive() for adventurer in self.party):
                self.save_simulation_results()
                break

    def all_enemies_dead(self, enemies):
        return not any(enemy.is_alive() for enemy in enemies)

    def all_adventurers_dead(self):
        return not any(adventurer.is_alive() for adventurer in self.party)

    def set_initiative_order(self) -> list[Creature]:
        # Roll initiative for the party
        for adventurer in self.party:
            adventurer.initiative = self.initiative_dice.roll() + adventurer.initiative_modifier

        # Roll initiative for the enemies
        for enemy in self.enemies:
            enemy.initiative = self.initiative_dice.roll() + enemy.initiative_modifier

        # Sort the party and enemies by initiative
        initiative_order: list[Creature] = self.party + self.enemies
        initiative_order.sort(key=lambda x: x.initiative, reverse=True)

        # Return the initiative order
        return initiative_order

    def save_simulation_results(self):
        self.simulation_count += 1
        self.simulation_results.total_simulations += 1
        if self.all_enemies_dead(self.enemies):
            self.simulation_results.remaining_hit_points_enemies.append(
                sum(enemy.hit_points for enemy in self.enemies if enemy.is_alive()))
            self.simulation_results.surviving_enemies.append(len([enemy for enemy in self.enemies if enemy.is_alive()]))
            self.simulation_results.encounters_lost += 1
        else:
            self.simulation_results.remaining_hit_points_adventurers.append(
                sum(adventurer.hit_points for adventurer in self.party if adventurer.is_alive()))
            self.simulation_results.surviving_adventurers.append(
                len([adventurer for adventurer in self.party if adventurer.is_alive()]))
            self.simulation_results.encounters_won += 1

    def print_results(self):
        # Iterate through the results and print the percentage won
        # The average amount of party members that survived the encounter
        print(f"\nResults:")
        print(f"Percentage of Encounters Won: "
              f"{self.simulation_results.encounters_won / self.simulation_results.total_simulations * 100}%")
        print(f"Percentage of Encounters Lost: "
              f"{self.simulation_results.encounters_lost / self.simulation_results.total_simulations * 100}%")
        print(f"Average Number of Party Members Surviving: "
              f"{sum(self.simulation_results.surviving_adventurers) / self.simulation_results.total_simulations} of {len(self.party)}")
        print(f"Average Number of Enemies Surviving: "
              f"{sum(self.simulation_results.surviving_enemies) / self.simulation_results.total_simulations}")
        print(f"Average Remaining Hit Points Enemies: "
              f"{sum(self.simulation_results.remaining_hit_points_enemies) / self.simulation_results.total_simulations}")
        print(f"Average Remaining Hit Points Adventurers: "
              f"{sum(self.simulation_results.remaining_hit_points_adventurers) / self.simulation_results.total_simulations} ")
