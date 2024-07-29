from enum import Enum


class ChallengeRating(Enum):
    """
    The challenge rating of a monster.

    :param challenge_rating: The challenge rating of the monster.
    :param experience_points: The experience points awarded for defeating the monster.
    :param proficiency_bonus: The proficiency bonus awarded for defeating the monster.
    """
    CR_0 = (0, 10, 2)
    CR_1_8 = (0.125, 25, 2)
    CR_1_4 = (0.25, 50, 2)
    CR_1_2 = (0.5, 100, 2)
    CR_1 = (1, 200, 2)
    CR_2 = (2, 450, 2)
    CR_3 = (3, 700, 2)
    CR_4 = (4, 1100, 2)
    CR_5 = (5, 1800, 3)
    CR_6 = (6, 2300, 3)
    CR_7 = (7, 2900, 3)
    CR_8 = (8, 3900, 3)
    CR_9 = (9, 5000, 4)
    CR_10 = (10, 5900, 4)
    CR_11 = (11, 7200, 4)
    CR_12 = (12, 8400, 4)
    CR_13 = (13, 10000, 5)
    CR_14 = (14, 11500, 5)
    CR_15 = (15, 13000, 5)
    CR_16 = (16, 15000, 5)
    CR_17 = (17, 18000, 6)
    CR_18 = (18, 20000, 6)
    CR_19 = (19, 22000, 6)
    CR_20 = (20, 25000, 6)
    CR_21 = (21, 33000, 7)
    CR_22 = (22, 41000, 7)
    CR_23 = (23, 50000, 7)
    CR_24 = (24, 62000, 7)
    CR_25 = (25, 75000, 8)
    CR_26 = (26, 90000, 8)
    CR_27 = (27, 105000, 8)
    CR_28 = (28, 120000, 8)
    CR_29 = (29, 135000, 9)
    CR_30 = (30, 155000, 9)

    def __init__(self, challenge_rating, experience_points, proficiency_bonus):
        self._challenge_rating = challenge_rating
        self._experience_points = experience_points
        self._proficiency_bonus = proficiency_bonus

    def get_challenge_rating(self) -> float:
        return self._challenge_rating

    def get_experience_points(self) -> int:
        return self._experience_points

    def get_proficiency_bonus(self) -> int:
        return self._proficiency_bonus
