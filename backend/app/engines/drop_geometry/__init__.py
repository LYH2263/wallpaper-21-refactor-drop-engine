"""Drop geometry primitives for wallpaper roll estimation.

Three independently testable pieces:

* :mod:`app.engines.drop_geometry.drops` -- drops around a perimeter
* :mod:`app.engines.drop_geometry.drop_len` -- length of one drop (height + pattern)
* :mod:`app.engines.drop_geometry.roll_strips` -- drops cut per roll / rolls needed
"""

from app.engines.drop_geometry.drops import drop_count
from app.engines.drop_geometry.drop_len import pattern_metres, strip_length
from app.engines.drop_geometry.roll_strips import rolls_needed, strips_per_roll

__all__ = [
    "drop_count",
    "pattern_metres",
    "strip_length",
    "strips_per_roll",
    "rolls_needed",
]
