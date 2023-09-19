"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

from dataclasses import dataclass
from typing import Union

import numpy as np

from trajectopy.util.definitions import Unit
from trajectopy.util.rotationset import RotationSet


@dataclass
class RPEResult:
    pos_dev: dict[float, list[float]]
    rot_dev: dict[float, list[float]]
    pair_distance: dict[float, list[float]]
    pair_distance_unit: Unit = Unit.METER

    @property
    def num_pairs(self) -> int:
        return sum(len(values) for values in self.pair_distance.values())


@dataclass
class ATEResult:
    pos_dev: np.ndarray
    directed_pos_dev: np.ndarray
    rot_dev: Union[RotationSet, None] = None
    rotations_used: bool = False
