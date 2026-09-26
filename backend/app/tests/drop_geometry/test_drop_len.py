"""drop_len 子模块测例: height + pattern repeat, including invalid repeats."""

import pytest

from app.engines.drop_geometry import pattern_metres, strip_length


def test_drop_len_matches_hand_fixtures(geometry_case):
    drop_len = strip_length(geometry_case["height"], geometry_case["pattern_cm"])
    assert round(drop_len, 3) == geometry_case["drop_len_m"]


def test_pattern_metres_matches_hand_fixtures(geometry_case):
    assert round(pattern_metres(geometry_case["pattern_cm"]), 3) == geometry_case["pattern_m"]


def test_plain_paper_adds_no_allowance():
    assert strip_length(2.7, 0) == 2.7
    assert pattern_metres(0) == 0.0


@pytest.mark.parametrize("bad_pattern", [-1, -64])
def test_negative_pattern_raises(bad_pattern):
    with pytest.raises(ValueError):
        pattern_metres(bad_pattern)
    with pytest.raises(ValueError):
        strip_length(2.7, bad_pattern)


def test_non_positive_drop_len_raises():
    with pytest.raises(ValueError):
        strip_length(0.0, 0)
