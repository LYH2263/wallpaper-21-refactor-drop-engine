"""每卷条数子模块测例: roll length / drop length, including invalid lengths."""

import pytest

from app.engines.drop_geometry import rolls_needed, strip_length, strips_per_roll


def test_strips_per_roll_matches_hand_fixtures(geometry_case):
    drop_len = strip_length(geometry_case["height"], geometry_case["pattern_cm"])
    assert strips_per_roll(geometry_case["roll_length"], drop_len) == geometry_case["strips_per_roll"]


def test_rolls_needed_matches_hand_fixtures(geometry_case):
    assert rolls_needed(geometry_case["drops"], geometry_case["strips_per_roll"]) == geometry_case["rolls"]


def test_roll_shorter_than_drop_still_yields_one_strip():
    assert strips_per_roll(2.0, 2.5) == 1


@pytest.mark.parametrize("bad_length", [0.0, -10.0])
def test_invalid_roll_length_raises(bad_length):
    with pytest.raises(ValueError):
        strips_per_roll(bad_length, 2.7)


def test_non_positive_drop_len_raises():
    with pytest.raises(ValueError):
        strips_per_roll(10.0, 0.0)


def test_invalid_strips_per_roll_raises():
    with pytest.raises(ValueError):
        rolls_needed(31, 0)
