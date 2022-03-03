from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from math import cos, sin, radians
from typing import Optional

# from attrs import define, field
from .location import Location

SAME_SPEED = -1.0
SAME_HEADING = -1.0
SAME_ALTITUDE = -1.0


class Movable(ABC):
    def __init__(self, id: str, name: str, max_speed: float):
        self.id = id
        self.name = name
        self.max_speed = max_speed
        self.t: Optional[datetime] = None
        self.location: Location = Location()
        self.is_deployed = False
        self.was_deployed = False
        self.speed = 0.0
        self.heading = 0.0
        self.history: list[Location] = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__} id: {self.id} name: {self.name}"

    def deploy(
        self, x: float, y: float, heading: float, speed: float, t: datetime
    ) -> bool:
        self.is_deployed = True
        self.was_deployed = True
        self.location = Location(x, y, t=t)
        self.heading = heading
        self.speed = speed
        self.t = t
        return True

    @abstractmethod
    def change(
        self, heading: float, speed: float, altitude: float, t: datetime
    ) -> bool:
        pass

    @abstractmethod
    def update_position(self, t: datetime) -> None:
        pass

    def print_history(self) -> None:
        for location in self.history:
            print(location)

    def _get_new_position(self, tm: datetime) -> Location:
        """Calculate a new position using 'dead reckoning'"""

        if self.t is None:
            return Location()
        if self.t == tm:
            return self.location

        tm_diff_in_hours = (tm - self.t) / timedelta(hours=1)
        distance = self.speed * tm_diff_in_hours
        dx = distance * sin(radians(self.heading))
        dy = distance * cos(radians(self.heading))
        return Location(
            x=self.location.x + dx, y=self.location.y + dy, z=self.location.z, t=tm
        )


class Ship(Movable):
    def change(
        self, heading: float, speed: float, altitude: float, t: datetime
    ) -> bool:
        # self.update_position(t)
        if heading != SAME_HEADING:
            self.heading = heading
        if speed != SAME_SPEED:
            self.speed = speed
        return True

    def update_position(self, t: datetime) -> None:
        self.location = self._get_new_position(t)
        self.history.append(self.location)
        self.t = t


class Cruiser(Ship):
    def __init__(self, id: str, name: str, max_speed: float, max_missiles: int):
        super().__init__(id, name, max_speed)
        self.max_missiles = max_missiles


class Carrier(Ship):
    def __init__(self, id: str, name: str, max_speed: float, max_aircraft: int):
        super().__init__(id, name, max_speed)
        self.max_aircraft = max_aircraft


# class Fighter(Movable):
#     def __init__(
#         self,
#         id: str,
#         name: str,
#         max_speed: float,
#         ship_id: str,
#         max_ceiling: float,
#         max_bombs: float,
#     ):
#         super().__init__(id, name, max_speed)
#         self.ship_id = ship_id
#         self.max_ceiling = max_ceiling
#         self.max_bombs = max_bombs
#         # maybe add a target altitude for smooth takeoff and landing
#         self.altitude = 0.0
#         self.ship_loc = Location()
#         self.is_landing = False

#     def deploy(
#         self, altitude: float, heading: float, speed: float, t: datetime
#     ) -> bool:
#         self.is_deployed = True
#         self.was_deployed = True
#         self.location = Location(self.ship_loc.x, self.ship_loc.y, altitude, t)
#         self.history.append(self.location)
#         self.heading = heading
#         self.speed = speed
#         self.altitude = altitude
#         self.t = t
#         return True

#     def change(
#         self, heading: float, speed: float, altitude: float, t: datetime
#     ) -> bool:
#         # self.update_position(t)
#         if speed != SAME_SPEED:
#             self.speed = speed

#         if altitude != SAME_ALTITUDE:
#             self.altitude = altitude

#         if not self.is_landing and heading != SAME_HEADING:
#             self.heading = heading

#         return True

#     def update_position(self, t: datetime) -> None:
#         pass
