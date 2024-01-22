from similator import Simulator

import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description="Simulate a D&D combat encounter.")

# Add an argument for the number of enemies
parser.add_argument("--enemy_count", type=int, help="The number of enemies in the encounter. Default is 4.")

# Add an argument for the number of simulations
parser.add_argument("--simulation_count", type=int, help="The number of simulations to run. Default is 100000.")

# Add an argument for the highest damage adventurers
parser.add_argument("--ad_highest_damage", action="store_true", help="If set, the adventuring party will only use their highest damage option. Default is False.")

# Add an argument for the highest damage enemies
parser.add_argument("--enemy_highest_damage", action="store_true", help="If set, the enemies will only use their highest damage option. Default is False.")

# Parse the arguments
args = parser.parse_args()

# Create a simulator object
simulator = Simulator(args.simulation_count, args.ad_highest_damage)

# Set the number of enemies
enemy_count = args.enemy_count

# Run the simulator
simulator.run(enemy_count)
