from seawarfare.movable import Carrier, Cruiser


def test_init_cruiser():
    cruiser = Cruiser(id="I264", name="Chelsey", max_speed=12.0, max_missiles=30)
    print(cruiser)
    assert cruiser is not None


def test_init_carrier():
    carrier = Carrier(id="P131", name="Gertrude", max_speed=25.0, max_aircraft=15)
    print(carrier)
    assert carrier is not None


# def test_init_fighter():
#     fighter = Fighter(
#         id="G264",
#         name="Brunhilde",
#         max_speed=500.0,
#         ship_id="P131",
#         max_ceiling=100000.0,
#         max_bombs=20,
#     )
#     print(fighter)
#     assert fighter is not None
