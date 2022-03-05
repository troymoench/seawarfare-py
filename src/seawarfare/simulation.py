from collections import deque
from datetime import datetime, timedelta
from pathlib import Path

from .movable import Movable
from .order import Order

# sim manager responsibilities
# parse order file
# create navy (movable) objects and add them to the "NavyMap"
# create orders and add them to the "OrderQueue"


class SimulationManager:
    def __init__(self) -> None:
        self.start = datetime(2000, 1, 1)
        self.stop = datetime(2000, 1, 1)
        self.navy_map: dict[str, Movable] = dict()
        self.order_queue: deque[Order] = deque()

    def print_orders(self) -> None:
        print(" Order Queue")
        print("=============")
        for order in self.order_queue:
            order.print()
        print("=============")

    def print_navy(self) -> None:
        print(" Navy Map")
        print("=============")
        for _, navy_obj in self.navy_map.items():
            print(navy_obj)
        print("=============")

    def print_history(self) -> None:
        for _, navy_obj in self.navy_map.items():
            print(navy_obj)
            navy_obj.print_history()

    def sim_init(self, order_file: Path) -> bool:
        with open(order_file, "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("#") or len(line.strip()) == 0:
                continue
            # split on whitespace
            tokens = line.split()
            print(tokens)
            opcode = tokens[0]
            if opcode == "StartSim":
                pass
            elif opcode == "StopSim":
                pass
            elif opcode == "CreateCruiser":
                pass
            elif opcode == "CreateAircraftCarrier":
                pass
            elif opcode == "CreateFighter":
                pass
            elif opcode == "DeployShip":
                pass
            elif opcode == "DeployAircraft":
                pass
            elif opcode == "ChangeShipOrders":
                pass
            elif opcode == "ChangeAircraftOrders":
                pass
            elif opcode == "LandAircraft":
                pass
            else:
                return False
        return True

    def do_update(self, t: datetime) -> None:
        pass

    def execute(self) -> None:
        print("starting sim")
        t = self.start
        while t < self.stop:
            self.do_update(t)
            t += timedelta(minutes=1)

        print("sim completed")
