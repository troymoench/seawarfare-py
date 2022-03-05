from pathlib import Path

from .simulation import SimulationManager


def main() -> None:
    sim = SimulationManager()
    sim.sim_init(Path("orders") / "orders01.txt")
    sim.print_navy()
    sim.print_orders()


if __name__ == "__main__":
    main()
