"""夹具驱动的几何链路测例：直接 import 几何包，不走 HTTP。"""

from app.engines.drop_geometry import (
    calc_drops,
    calc_drop_len,
    calc_rolls,
    calc_strips_per_roll,
    pattern_repeat_m,
)
from app.engines.wallpaper_math import roll_count


def _run_chain(geom):
    pattern_m = pattern_repeat_m(geom["pattern_cm"])
    drop_len = calc_drop_len(geom["height"], pattern_m)
    strips_per_roll = calc_strips_per_roll(geom["roll_length"], drop_len)
    drops = calc_drops(geom["perimeter"], geom["roll_width"])
    return drops, pattern_m, drop_len, strips_per_roll, calc_rolls(drops, strips_per_roll)


def test_big_pattern_wall_fixture(big_pattern_wall):
    drops, pattern_m, drop_len, strips, rolls = _run_chain(big_pattern_wall)
    expect = big_pattern_wall["expect"]
    assert drops == expect["drops"]
    assert round(pattern_m, 3) == expect["pattern_m"]
    assert round(drop_len, 3) == expect["drop_len"]
    assert strips == expect["strips_per_roll"]
    assert rolls == expect["rolls"]


def test_plain_master_bed_geometry_fixture(plain_master_bed_geometry):
    drops, _, drop_len, strips, rolls = _run_chain(plain_master_bed_geometry)
    expect = plain_master_bed_geometry["expect"]
    assert (drops, round(drop_len, 3), strips, rolls) == (
        expect["drops"],
        expect["drop_len"],
        expect["strips_per_roll"],
        expect["rolls"],
    )


def test_short_wall_geometry_fixture(short_wall_geometry):
    drops, pattern_m, drop_len, strips, rolls = _run_chain(short_wall_geometry)
    expect = short_wall_geometry["expect"]
    assert (drops, round(pattern_m, 3), round(drop_len, 3), strips, rolls) == (
        expect["drops"],
        expect["pattern_m"],
        expect["drop_len"],
        expect["strips_per_roll"],
        expect["rolls"],
    )


def test_roll_count_matches_big_pattern_fixture(big_pattern_wall):
    g = big_pattern_wall
    r = roll_count(g["perimeter"], g["height"], g["roll_width"], g["roll_length"], g["pattern_cm"])
    assert r == {
        "drops": 38,
        "drop_len_m": 3.44,
        "pattern_m": 0.64,
        "strips_per_roll": 2,
        "rolls": 19,
    }
