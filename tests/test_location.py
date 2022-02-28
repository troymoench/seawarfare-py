from pytest import approx
from seawarfare.location import Location


def test_location_distance():
    a = Location(x=1, y=1, z=0)
    b = Location(x=2, y=2, z=0)
    assert a.distance(b) == approx(1.414214)
