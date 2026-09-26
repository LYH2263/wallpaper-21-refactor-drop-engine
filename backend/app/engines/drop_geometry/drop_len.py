"""Length of a single wallpaper drop: wall height plus pattern-match allowance."""


def pattern_metres(pattern_cm: float) -> float:
    """Convert a pattern repeat in centimetres to metres (negative repeats are invalid)."""
    pattern = float(pattern_cm)
    if pattern < 0:
        raise ValueError("invalid pattern repeat")
    return max(0.0, pattern / 100.0)


def strip_length(height: float, pattern_cm: float) -> float:
    """Wall height plus the pattern repeat allowance; must stay strictly positive."""
    drop_len = float(height) + pattern_metres(pattern_cm)
    if drop_len <= 0:
        raise ValueError("invalid drop length")
    return drop_len
