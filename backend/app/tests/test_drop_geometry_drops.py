import pytest

from app.engines.drop_geometry import calc_drops


def test_whole_widths():
    assert calc_drops(4.0, 0.5) == 8


def test_partial_width_rounds_up():
    # 16 / 0.53 = 30.19 → 31 条
    assert calc_drops(16.0, 0.53) == 31


def test_zero_perimeter_is_zero_drops():
    assert calc_drops(0.0, 0.53) == 0


@pytest.mark.parametrize("bad_width", [0, 0.0, -0.53])
def test_invalid_roll_width_raises(bad_width):
    with pytest.raises(ValueError, match="invalid roll width"):
        calc_drops(16.0, bad_width)


def test_negative_perimeter_raises():
    with pytest.raises(ValueError, match="invalid perimeter"):
        calc_drops(-1.0, 0.53)
