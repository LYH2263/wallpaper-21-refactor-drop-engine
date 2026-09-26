import pytest

from app.engines.drop_geometry import calc_drop_len, pattern_repeat_m


def test_pattern_cm_to_m():
    assert pattern_repeat_m(64) == pytest.approx(0.64)


def test_zero_pattern_is_zero_m():
    assert pattern_repeat_m(0) == 0.0


def test_drop_len_adds_one_repeat():
    assert calc_drop_len(2.8, 0.64) == pytest.approx(3.44)


def test_plain_drop_len_equals_height():
    assert calc_drop_len(2.7, 0.0) == pytest.approx(2.7)


def test_negative_pattern_cm_raises():
    with pytest.raises(ValueError, match="invalid pattern repeat"):
        pattern_repeat_m(-1)


def test_negative_pattern_m_raises():
    with pytest.raises(ValueError, match="invalid pattern repeat"):
        calc_drop_len(2.7, -0.1)


@pytest.mark.parametrize("height,pattern_m", [(0.0, 0.0), (-2.7, 0.0), (0.0, -0.0)])
def test_non_positive_drop_len_raises(height, pattern_m):
    with pytest.raises(ValueError, match="invalid drop length"):
        calc_drop_len(height, pattern_m)
