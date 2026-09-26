"""drops 子模块测例: perimeter / roll width, including invalid widths."""

import pytest

from app.engines.drop_geometry import drop_count


def test_drops_match_hand_fixtures(geometry_case):
    assert drop_count(geometry_case["perimeter"], geometry_case["roll_width"]) == geometry_case["drops"]


def test_master_bed_plain53(master_bed_case):
    assert drop_count(master_bed_case["perimeter"], master_bed_case["roll_width"]) == 31


def test_big_flower_wall(big_flower_case):
    assert drop_count(big_flower_case["perimeter"], big_flower_case["roll_width"]) == 38


def test_zero_perimeter_needs_no_drops():
    assert drop_count(0.0, 0.53) == 0


@pytest.mark.parametrize("bad_width", [0.0, -0.53])
def test_invalid_roll_width_raises(bad_width):
    with pytest.raises(ValueError):
        drop_count(16.0, bad_width)


def test_negative_perimeter_raises():
    with pytest.raises(ValueError):
        drop_count(-1.0, 0.53)
