# encounter-simulator-5e

A simple encounter simulator for D&D 5e, where a set group of monsters fight another set group of monsters.

## Usage

To run the simulator, simply run the following command:

```bash
python3 main.py
```

Additionally, you can specify a few optional arguments:

- `--simulation-count` to specify the number of simulations to run.

```bash
python3 main.py --simulation-count 1000
```

## Example

Here is an example of the simulator in action:

```bash
$ python3 main.py
Simulation 1564 of 10000 Simulations
{'party_1_wins': 32953, 'party_2_wins': 67047}
```

## Contributing

If you would like to contribute, please open an issue or a pull request.

## Roadmap

- [ ] Add graphical interface for easier use (Website)
- [ ] Add support for distance tracking (Virtual Tabletop)
- [ ] Add support for spellcasting
- [ ] Add support for condition effects
- [ ] Add support for legendary actions
- [ ] Add support for lair actions
- [ ] Add ability to add player characters
    - [ ] Artificer
    - [ ] Barbarian
    - [ ] Bard
    - [ ] Blood Hunter
    - [ ] Cleric
    - [ ] Druid
    - [ ] Fighter
    - [ ] Monk
    - [ ] Paladin
    - [ ] Ranger
    - [ ] Rogue
    - [ ] Sorcerer
    - [ ] Warlock
    - [ ] Wizard
    - [ ] Custom
- [ ] Add ability to save and load encounters
- [ ] Add support for homebrew monsters, spells, items, etc.
