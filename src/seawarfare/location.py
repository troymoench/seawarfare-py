from __future__ import annotations
from datetime import datetime
from math import sqrt
from attrs import define


@define(kw_only=True)
class Location:
    x: float = 0
    y: float = 0
    z: float = 0
    t: datetime = datetime(2000, 1, 1)

    def distance(self, other: Location) -> float:
        """Calculate the 2D distance between two locations using the Pythagorean Theorem"""
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(pow(dx, 2) + pow(dy, 2))
