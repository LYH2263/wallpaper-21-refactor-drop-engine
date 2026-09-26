"""每卷可裁条数：卷长 ÷ 条长；总卷数再按分幅数汇总。"""

from app.engines.helpers import ceil_units, floor_units


def calc_strips_per_roll(roll_length: float, drop_len: float) -> int:
    """一卷纸能裁出的整条数，至少按 1 条计。"""
    roll_length = float(roll_length)
    drop_len = float(drop_len)
    if roll_length <= 0:
        raise ValueError("invalid roll length")
    if drop_len <= 0:
        raise ValueError("invalid drop length")
    return max(1, floor_units(roll_length / drop_len))


def calc_rolls(drops: int, strips_per_roll: int) -> int:
    """总卷数 = 分幅数 ÷ 每卷条数，不足一卷按一卷计。"""
    drops = int(drops)
    strips_per_roll = int(strips_per_roll)
    if strips_per_roll <= 0:
        raise ValueError("invalid strips per roll")
    return ceil_units(drops / strips_per_roll)
