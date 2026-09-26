"""Number of wallpaper drops (vertical strips) needed around a perimeter."""

from app.engines.helpers import ceil_units


def drop_count(perimeter: float, roll_width: float) -> int:
    """Ceiling of perimeter divided by the roll (strip) width."""
    width = float(roll_width)
    if width <= 0:
        raise ValueError("invalid roll width")
    if float(perimeter) < 0:
        raise ValueError("invalid perimeter")
    return ceil_units(float(perimeter) / width)
