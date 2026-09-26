"""Wallpaper rolls: validate estimate inputs and orchestrate drop geometry.

All arithmetic lives in :mod:`app.engines.drop_geometry`; this module only
checks the raw inputs and serially wires drops -> drop length -> strips/rolls.
"""

from app.engines.drop_geometry import (
    drop_count,
    pattern_metres,
    rolls_needed,
    strips_per_roll,
    strip_length,
)


def roll_count(
    perimeter: float,
    height: float,
    roll_width: float,
    roll_length: float,
    pattern_cm: float,
) -> dict:
    drops = drop_count(perimeter, roll_width)
    pattern_m = pattern_metres(pattern_cm)
    drop_len = strip_length(height, pattern_cm)
    per_roll = strips_per_roll(roll_length, drop_len)
    rolls = rolls_needed(drops, per_roll)
    return {
        "drops": drops,
        "drop_len_m": round(drop_len, 3),
        "pattern_m": round(pattern_m, 3),
        "strips_per_roll": per_roll,
        "rolls": rolls,
    }
