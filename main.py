from simulator import Simulator
import argparse
import sys

# Create an argument parser
parser = argparse.ArgumentParser(description="Simulate a D&D combat encounter.")

# Add an argument for the number of enemies
parser.add_argument("--enemy_count", type=int, default=4, help="The number of enemies in the encounter. Default is 4.")

# Add an argument for the number of simulations
parser.add_argument("--simulation_count", type=int, default=100000, help="The number of simulations to run. Default is 100000.")

# Add an argument for the highest damage adventurers
parser.add_argument("--adventurers_highest_damage", action="store_true", help="If set, the adventuring party will only use their highest damage option. Default is False.")

# Add an argument for the highest damage enemies
parser.add_argument("--enemies_highest_damage", action="store_true", help="If set, the enemies will only use their highest damage option. Default is False.")

# Parse the arguments
args = parser.parse_args()

# Check if the arguments are within an acceptable range
if args.enemy_count < 1 or args.simulation_count < 1:
    print("Error: The number of enemies and simulations must be greater than 0.")
    sys.exit(1)

# Create a simulator object
simulator = Simulator(args.simulation_count, args.adventurers_highest_damage)

# Set the number of enemies
enemy_count = args.enemy_count

# Run the simulator
simulator.run(enemy_count)