from similator import Simulator

# Create a simulator object
simulator = Simulator(100000)

# Set the number of enemies
enemy_count = int(input("How many enemies?: "))

# Run the simulator
simulator.run(enemy_count)