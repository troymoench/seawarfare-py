from datetime import datetime

from seawarfare.order import DeployShip


def test_create_deploy_ship():
    tm = datetime(2015, 10, 21, 17, 2, 0)
    order = DeployShip(
        id="CGN-39", extime=tm, start_x=0.0, start_y=0.0, heading=0.0, speed=50
    )
    order.print()
    assert order.get_id() == "CGN-39"
    assert order.get_extime() == datetime(2015, 10, 21, 17, 2, 0)
