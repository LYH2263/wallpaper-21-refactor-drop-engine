"""单条裁切长度：层高 + 花高（花距厘米换算成米）。"""


def pattern_repeat_m(pattern_cm: float) -> float:
    """花高（花距）由厘米换算为米，不允许负值。"""
    pattern_cm = float(pattern_cm)
    if pattern_cm < 0:
        raise ValueError("invalid pattern repeat")
    return max(0.0, pattern_cm / 100.0)


def calc_drop_len(height: float, pattern_m: float) -> float:
    """每条墙纸的裁切长度 = 层高 + 一个花高。"""
    height = float(height)
    pattern_m = float(pattern_m)
    if pattern_m < 0:
        raise ValueError("invalid pattern repeat")
    drop_len = height + pattern_m
    if drop_len <= 0:
        raise ValueError("invalid drop length")
    return drop_len
