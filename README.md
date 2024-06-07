# encounter-simulator-5e

A simple encounter simulator for D&D 5e, where a set party of characters fights a set group of goblins.

## Usage

To run the simulator, simply run the following command:

```bash
python3 main.py
```

Additionally, you can specify a few optional arguments:

- `--enemy-count` to specify the number of enemies in the encounter.
- `--simulation-count` to specify the number of simulations to run.
- `--adventures-highest-damage` to specify that the adventuring party will only use their highest damage option.
- `--enemies-highest-damage` to specify that the enemies will only use their highest damage option.

```bash
python3 main.py --enemy-count 3 --simulation-count 1000 --adventures-highest-damage --enemies-highest-damage
```
