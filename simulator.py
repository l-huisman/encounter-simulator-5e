from models.dice import Dice
from models.action import Action
from models.creature import Creature
from results import SimulationResults

import random


class Simulator:
    def __init__(self, total_simulations, adventurers_highest_damage):
        self.simulation_count = 0
        self.initiative_dice = Dice(1, 20)
        self.total_simulations = total_simulations
        self.adventurers_highest_damage = adventurers_highest_damage
        self.simulation_results = SimulationResults()

    def run(self, enemy_count):
        # Run the simulation until the simulation count
        while self.simulation_count < self.total_simulations:
            # Create the list of enemies
            enemies: list[Creature] = []
            for i in range(enemy_count):
                enemies.append(Creature("Goblin", [Action("Scimitar", 2, 2, Dice(1, 6)), Action("Longbow", 2, 2, Dice(1, 8))], 7, 15, 2))

            # Create an adventuring party
            party: list[Creature] = [
                Creature("Fighter", [Action("Longsword", 2, 3, Dice(1, 8)), Action("Shortbow", 2, 2, Dice(1, 6))], 13, 18, 2),
                Creature("Rogue", [Action("Shortsword", 2, 3, Dice(1, 6)), Action("Shortbow", 2, 3, Dice(1, 6))], 11, 15, 3),
                Creature("Wizard", [Action("Firebolt", 2, 3, Dice(1, 10)), Action("Chill Touch", 2, 3, Dice(1, 8))], 9, 12, 1),
                Creature("Cleric", [Action("Mace", 2, 1, Dice(1, 6)), Action("Longbow", 2, 0, Dice(1, 8))], 10, 16, 0),
            ]

            if self.simulation_count % 10000 == 0:
                print(f"\rSimulation {self.simulation_count} of {self.total_simulations}")

            # Set initiative order
            initiative_order = self.set_initiative_order(party, enemies)

            # Set the round to 0
            self.round = 1

            # Encounter loop
            while True:
                # Iterate through the initiative order
                for creature in initiative_order:
                    # If the creature is dead, skip their turn
                    if not creature.is_alive():
                        continue

                    # If the creature is an enemy, attack a random adventurer
                    if creature in enemies:
                        target: Creature = random.choice(party)
                        creature.attack(target)
                    else:  # If the creature is an adventurer, attack a random enemy
                        target: Creature = random.choice(enemies)
                        creature.attack(target)

                    # If all the enemies or all the adventurers are dead, end the combat
                    if not any(enemy.is_alive() for enemy in enemies) or not any(adventurer.is_alive() for adventurer in party):
                        break

                # Increment the round
                self.round += 1

                # If all the enemies are dead, end the combat
                if not any(enemy.is_alive() for enemy in enemies) or not any(adventurer.is_alive() for adventurer in party):
                    self.save_simulation_results(enemies, party)
                    break

        # Print the results
        self.print_results()

    def save_simulation_results(self, enemies: list[Creature], party: list[Creature]):
        self.simulation_count += 1
        self.simulation_results.total_simulations += 1
        if any(enemy.is_alive() for enemy in enemies):
            self.simulation_results.remaining_hit_points_enemies.append(sum(enemy.hit_points for enemy in enemies if enemy.is_alive()))
            self.simulation_results.surviving_enemies.append(len([enemy for enemy in enemies if enemy.is_alive()]))
            self.simulation_results.encounters_lost += 1
        else:
            self.simulation_results.remaining_hit_points_adventurers.append(sum(adventurer.hit_points for adventurer in party if adventurer.is_alive()))
            self.simulation_results.surviving_adventurers.append(len([adventurer for adventurer in party if adventurer.is_alive()]))
            self.simulation_results.encounters_won += 1

    def set_initiative_order(self, party, enemies):
        # Roll initative for the party
        for adventurer in party:
            adventurer.initiative = self.initiative_dice.roll() + adventurer.initiative_modifier

        # Roll initative for the enemies
        for enemy in enemies:
            enemy.initiative = self.initiative_dice.roll() + enemy.initiative_modifier

        # Sort the party and enemies by initative
        initiative_order: list[Creature] = party + enemies
        initiative_order.sort(key=lambda x: x.initiative, reverse=True)

        # Return the initiative order
        return initiative_order

    def print_results(self):
        # Iterate through the results and print the percentage won
        # The average amount of party members that survived the encounter
        print(f"\nResults:")
        print(f"Percentage of Encounters Won: {self.simulation_results.encounters_won / self.simulation_results.total_simulations * 100}%")
        print(f"Percentage of Encounters Lost: {self.simulation_results.encounters_lost / self.simulation_results.total_simulations * 100}%")
        print(f"Average Number of Party Members Surviving: {sum(self.simulation_results.surviving_adventurers) / self.simulation_results.total_simulations}")
        print(f"Average Number of Enemies Surviving: {sum(self.simulation_results.surviving_enemies) / self.simulation_results.total_simulations}")
        print(f"Average Remaining Hit Points Enemies: {sum(self.simulation_results.remaining_hit_points_enemies) / self.simulation_results.total_simulations}")
        print(f"Average Remaining Hit Points Adventurers: {sum(self.simulation_results.remaining_hit_points_adventurers) / self.simulation_results.total_simulations} ")
