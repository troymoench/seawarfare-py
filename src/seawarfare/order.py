from abc import ABC
from datetime import datetime

from attrs import define


@define
class Order(ABC):
    id: str
    extime: datetime

    def get_id(self) -> str:
        return self.id

    def get_extime(self) -> datetime:
        return self.extime

    def print(self) -> None:
        print(f"id: {self.id} extime: {self.extime}")


@define
class DeployShip(Order):
    start_x: float
    start_y: float
    heading: float
    speed: float


@define
class DeployAircraft(Order):
    heading: float
    speed: float
    altitude: float


@define
class ChangeShip(Order):
    heading: float
    speed: float


@define
class ChangeAircraft(Order):
    heading: float
    speed: float
    altitude: float


@define
class LandAircraft(Order):
    ship_id: str
