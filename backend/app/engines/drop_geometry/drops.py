"""分幅条数：周长 ÷ 幅宽。"""

from app.engines.helpers import ceil_units


def calc_drops(perimeter: float, roll_width: float) -> int:
    """一圈墙需要的分幅（条）数，不足一幅按一幅计。"""
    perimeter = float(perimeter)
    roll_width = float(roll_width)
    if roll_width <= 0:
        raise ValueError("invalid roll width")
    if perimeter < 0:
        raise ValueError("invalid perimeter")
    return ceil_units(perimeter / roll_width)
