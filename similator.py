from dice import Dice
from action import Action
from creature import Creature

import random


class Simulator:
    def __init__(self, total_simulations):
        self.simulation_count = 0
        self.simulation_results = []
        self.initiative_dice = Dice(1, 20)
        self.total_simulations = total_simulations

    def run(self, enemy_count):
        # Run the simulation until the simulation count
        while self.simulation_count < self.total_simulations:
            # Create the list of enemies
            enemies: list[Creature] = []
            for i in range(enemy_count):
                enemies.append(Creature("Goblin", [Action("Scimitar", 2, 2, Dice(1, 6))], 7, 15, 2))

            # Create an adventuring party
            party: list[Creature] = [
                Creature("Fighter", [Action("Longsword", 2, 3, Dice(1, 8))], 13, 18, 2),
                Creature("Rogue", [Action("Shortsword", 2, 3, Dice(1, 6))], 11, 15, 3),
                Creature("Wizard", [Action("Firebolt", 2, 3, Dice(1, 10))], 9, 12, 1),
                Creature("Cleric", [Action("Mace", 2, 1, Dice(1, 6))], 10, 16, 0),
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
                    self.simulation_results.append(len([adventurer for adventurer in party if adventurer.is_alive()]))
                    self.simulation_count += 1
                    break

        # Print the results
        self.print_results()

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
        print(f"Percentage of Encounters Won: {len([result for result in self.simulation_results if result > 0]) / len(self.simulation_results) * 100}%")
        print(f"Percentage of Encounters Lost: {len([result for result in self.simulation_results if result == 0]) / len(self.simulation_results) * 100}%")
