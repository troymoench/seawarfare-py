from seawarfare.simulation import SimulationManager


def test_init_simulation_manager():
    sim_manager = SimulationManager()
    assert sim_manager is not None
