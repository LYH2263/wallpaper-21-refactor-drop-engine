"""分幅几何包：分幅条数、条长（对花）、每卷条数与总卷数。"""

from app.engines.drop_geometry.drops import calc_drops
from app.engines.drop_geometry.drop_length import calc_drop_len, pattern_repeat_m
from app.engines.drop_geometry.strips import calc_rolls, calc_strips_per_roll

__all__ = [
    "calc_drops",
    "calc_drop_len",
    "pattern_repeat_m",
    "calc_strips_per_roll",
    "calc_rolls",
]
