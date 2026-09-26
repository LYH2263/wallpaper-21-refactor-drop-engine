"""How many drops fit on one roll, and how many rolls the job consumes."""

from app.engines.helpers import ceil_units, floor_units


def strips_per_roll(roll_length: float, drop_len: float) -> int:
    """Floor of roll length divided by drop length; at least one strip per roll."""
    length = float(roll_length)
    drop = float(drop_len)
    if length <= 0:
        raise ValueError("invalid roll length")
    if drop <= 0:
        raise ValueError("invalid drop length")
    return max(1, floor_units(length / drop))


def rolls_needed(drops: int, per_roll: int) -> int:
    """Ceiling of total drops divided by strips cut from one roll."""
    if per_roll <= 0:
        raise ValueError("invalid strips per roll")
    if drops < 0:
        raise ValueError("invalid drops")
    return ceil_units(drops / per_roll)
