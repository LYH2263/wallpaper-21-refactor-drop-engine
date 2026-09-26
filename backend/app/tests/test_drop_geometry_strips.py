import pytest

from app.engines.drop_geometry import calc_rolls, calc_strips_per_roll


def test_plain_strips_per_roll():
    # floor(10 / 2.7) = 3
    assert calc_strips_per_roll(10.0, 2.7) == 3


def test_pattern_strips_per_roll():
    # floor(10 / 3.44) = 2
    assert calc_strips_per_roll(10.0, 3.44) == 2


def test_drop_longer_than_roll_still_one_strip():
    assert calc_strips_per_roll(5.0, 6.0) == 1


@pytest.mark.parametrize("bad_length", [0, 0.0, -10.0])
def test_invalid_roll_length_raises(bad_length):
    with pytest.raises(ValueError, match="invalid roll length"):
        calc_strips_per_roll(bad_length, 2.7)


@pytest.mark.parametrize("bad_drop_len", [0, 0.0, -2.7])
def test_invalid_drop_len_raises(bad_drop_len):
    with pytest.raises(ValueError, match="invalid drop length"):
        calc_strips_per_roll(10.0, bad_drop_len)


def test_rolls_total():
    assert calc_rolls(31, 3) == 11
    assert calc_rolls(38, 2) == 19


def test_invalid_strips_per_roll_raises():
    with pytest.raises(ValueError, match="invalid strips per roll"):
        calc_rolls(10, 0)
