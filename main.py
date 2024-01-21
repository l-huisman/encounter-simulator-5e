from creature import Creature
from action import Action
from dice import Dice

import time
import random


def main() -> None:
    # Get the number of enemies
    enemy_count: int = int(input("How many enemies?: "))

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

    # Create the initiative dice
    initiative_dice: Dice = Dice(1, 20)

    # Roll initative for the party
    for adventurer in party:
        adventurer.initiative = initiative_dice.roll() + adventurer.initiative_modifier

    # Roll initative for the enemies
    for enemy in enemies:
        enemy.initiative = initiative_dice.roll() + enemy.initiative_modifier

    # Sort the party and enemies by initative
    initiative_order: list[Creature] = party + enemies
    initiative_order.sort(key=lambda x: x.initiative, reverse=True)

    # Print the initiative order
    print("\nInitiative Order:")
    for creature in initiative_order:
        print(f"{creature.name}: {creature.initiative}")


    print("\nCombat Begins in 5 seconds!")
    time.sleep(5)

    round = 1

    # Combat loop
    while True:
        # Iterate through the initiative order
        print(f"\nRound {round}:")
        for creature in initiative_order:
            # If the creature is dead, skip their turn
            if not creature.is_alive():
                continue

            # If the creature is an enemy, attack a random adventurer
            if creature in enemies:
                target: Creature = random.choice(party)
                creature.attack(target)
            # If the creature is an adventurer, attack a random enemy
            else:
                target: Creature = random.choice(enemies)
                creature.attack(target)

            # If all the enemies are dead, end the combat
            if not any(enemy.is_alive() for enemy in enemies):
                print("The enemies are dead!")
                exit()

            # If all the adventurers are dead, end the combat
            if not any(adventurer.is_alive() for adventurer in party):
                print("The adventurers are dead!")
                exit()

            # Wait for 2 seconds
            time.sleep(2)
        round += 1


if __name__ == "__main__":
    main()
