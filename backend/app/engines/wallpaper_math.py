"""Wallpaper rolls: 入参校验 + 串调 drop_geometry 各子模块。"""

from app.engines.drop_geometry import (
    calc_drops,
    calc_drop_len,
    calc_rolls,
    calc_strips_per_roll,
    pattern_repeat_m,
)


def roll_count(
    perimeter: float,
    height: float,
    roll_width: float,
    roll_length: float,
    pattern_cm: float,
) -> dict:
    perimeter = float(perimeter)
    height = float(height)
    roll_width = float(roll_width)
    roll_length = float(roll_length)
    pattern_cm = float(pattern_cm)
    if roll_width <= 0:
        raise ValueError("invalid roll width")
    if roll_length <= 0:
        raise ValueError("invalid roll length")
    if perimeter < 0:
        raise ValueError("invalid perimeter")
    if height < 0:
        raise ValueError("invalid height")
    if pattern_cm < 0:
        raise ValueError("invalid pattern repeat")

    drops = calc_drops(perimeter, roll_width)
    pattern_m = pattern_repeat_m(pattern_cm)
    drop_len = calc_drop_len(height, pattern_m)
    strips_per_roll = calc_strips_per_roll(roll_length, drop_len)
    rolls = calc_rolls(drops, strips_per_roll)
    return {
        "drops": drops,
        "drop_len_m": round(drop_len, 3),
        "pattern_m": round(pattern_m, 3),
        "strips_per_roll": strips_per_roll,
        "rolls": rolls,
    }
