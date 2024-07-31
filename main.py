import argparse
import sys
from typing import List

from constants.challenge_rating import ChallengeRating
from constants.damage_type import DamageType
from constants.item_rarity import ItemRarity
from constants.weapon_property import WeaponProperty
from constants.weapon_type import WeaponType
from models.action import Action
from models.dice import Dice
from models.monster import Monster
from models.weapon import Weapon
from simulator import Simulator

parser = argparse.ArgumentParser(description="Simulate a D&D combat encounter.")
parser.add_argument("--simulation-count", type=int, default=100000,
                    help="The number of simulations to run. Default is 100000.")
args = parser.parse_args()

# Check if the arguments are within an acceptable range
if args.simulation_count < 1:
    print("Error: The number of enemies and simulations must be greater than 0.")
    sys.exit(1)

long_sword = Weapon("long-sword", WeaponType.MARTIAL_MELEE, Dice(1, 8), DamageType.SLASHING, ItemRarity.COMMON, [WeaponProperty.VERSATILE, WeaponProperty.TWO_HANDED], 5, 3)

goblin = Monster(name="Goblin", size="Small", race="Humanoid (Goblinoid)", sub_race="", alignment="Neutral Evil",
                 strength=8, dexterity=14, constitution=10, intelligence=10, wisdom=8, charisma=8, hit_dice=Dice(2, 6),
                 armour_class=15, speed=30, skills={}, senses={"darkvision": 60}, languages=["Common", "Goblin"],
                 challenge_rating=ChallengeRating.CR_1_4, damage_vulnerabilities=[], damage_resistances=[],
                 damage_immunities=[], condition_immunities=[], special_abilities=[], actions=[
        Action(name="Scimitar", proficiency_modifier=2, ability_modifier=2, damage_dice=Dice(1, 6)),
        Action(name="Shortbow", proficiency_modifier=2, ability_modifier=2, damage_dice=Dice(1, 6))],
                 bonus_actions=[], legendary_actions=[], reactions=[])

bugbear = Monster(name="Bugbear", size="Medium", race="Humanoid (Goblinoid)", sub_race="", alignment="Chaotic Evil",
                  strength=16, dexterity=14, constitution=15, intelligence=8, wisdom=11, charisma=9,
                  hit_dice=Dice(4, 8),
                  armour_class=16, speed=30, skills={"Stealth": 6}, senses={"darkvision": 60},
                  languages=["Common", "Goblin"],
                  challenge_rating=ChallengeRating.CR_1, damage_vulnerabilities=[], damage_resistances=[],
                  damage_immunities=[],
                  condition_immunities=[], special_abilities=[], actions=[
        Action(name="Morningstar", proficiency_modifier=3, ability_modifier=3, damage_dice=Dice(1, 8)),
        Action(name="Javelin", proficiency_modifier=3, ability_modifier=3, damage_dice=Dice(1, 6))],
                  bonus_actions=[], legendary_actions=[], reactions=[])

party_1: List[Monster] = [
    goblin, goblin, goblin, goblin
]

party_2: List[Monster] = [
    bugbear
]

simulator = Simulator(args.simulation_count, party_1, party_2)

simulator.run()
