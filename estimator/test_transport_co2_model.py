from transport_co2.model import Mode

# Only distance
def test_estimate_co2_bus():
    co2_estimate = Mode["BUS"].estimate_co2(distance_in_km=10)

    assert co2_estimate == 679.5275590551181


def test_estimate_co2_light_rail():
    co2_estimate = Mode["LIGHT_RAIL"].estimate_co2(distance_in_km=10)

    assert co2_estimate == 140


def test_estimate_co2_small_car():
    co2_estimate = Mode["SMALL_CAR"].estimate_co2(distance_in_km=10)

    assert co2_estimate == 1120


def test_estimate_co2_large_car():
    co2_estimate = Mode["LARGE_CAR"].estimate_co2(distance_in_km=10)

    assert co2_estimate == 1466.6666666666667


def test_estimate_co2_scooter():
    co2_estimate = Mode["SCOOTER"].estimate_co2(distance_in_km=10)

    assert co2_estimate == 720


# Distance and occupancy
def test_estimate_co2_bus_with_occupancy():
    co2_estimate = Mode["BUS"].estimate_co2(distance_in_km=10, occupancy=10)

    assert co2_estimate == 863


def test_estimate_co2_light_rail_with_occupancy():
    co2_estimate = Mode["LIGHT_RAIL"].estimate_co2(distance_in_km=10, occupancy=100)

    assert co2_estimate == 218.4


def test_estimate_co2_small_car_with_occupancy():
    co2_estimate = Mode["SMALL_CAR"].estimate_co2(distance_in_km=10, occupancy=2)

    assert co2_estimate == 840.0


def test_estimate_co2_large_car_with_occupancy():
    co2_estimate = Mode["LARGE_CAR"].estimate_co2(distance_in_km=10, occupancy=3)

    assert co2_estimate == 733.3333333333334


def test_estimate_co2_scooter_with_occupancy():
    co2_estimate = Mode["SCOOTER"].estimate_co2(distance_in_km=10, occupancy=2)

    assert co2_estimate == 432.0
