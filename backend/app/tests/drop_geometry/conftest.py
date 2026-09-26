"""Hand-written geometry fixtures (夹具) for the drop_geometry test suite.

Every expected number below is computed by hand, so the tests double as
executable documentation of the geometry the engine must reproduce.
"""

import pytest

# 主卧一圈 × 素色53: plain paper, no pattern repeat.
MASTER_BED_PLAIN53 = {
    "name": "主卧一圈×素色53",
    "perimeter": 16.0, "height": 2.7,
    "roll_width": 0.53, "roll_length": 10.0, "pattern_cm": 0,
    "drops": 31, "drop_len_m": 2.7, "pattern_m": 0.0,
    "strips_per_roll": 3, "rolls": 11,
}

# 大花匹配 × 大花64: 64cm repeat padded onto every drop.
BIG_FLOWER_WALL = {
    "name": "大花匹配×大花64",
    "perimeter": 20.0, "height": 2.8,
    "roll_width": 0.53, "roll_length": 10.0, "pattern_cm": 64,
    "drops": 38, "drop_len_m": 3.44, "pattern_m": 0.64,
    "strips_per_roll": 2, "rolls": 19,
}

# hand-written: every division lands exactly, nothing rounds up.
EXACT_FIT = {
    "name": "hand-exact-fit",
    "perimeter": 10.6, "height": 2.5,
    "roll_width": 0.53, "roll_length": 12.0, "pattern_cm": 50,
    "drops": 20, "drop_len_m": 3.0, "pattern_m": 0.5,
    "strips_per_roll": 4, "rolls": 5,
}

# hand-written: perimeter and roll length both leave remainders.
REMAINDER_ROUND_UP = {
    "name": "hand-remainder-round-up",
    "perimeter": 7.0, "height": 2.6,
    "roll_width": 0.53, "roll_length": 10.0, "pattern_cm": 32,
    "drops": 14, "drop_len_m": 2.92, "pattern_m": 0.32,
    "strips_per_roll": 3, "rolls": 5,
}

# hand-written: roll shorter than one drop still yields a strip (max-1 guard).
SHORT_ROLL = {
    "name": "hand-short-roll",
    "perimeter": 4.0, "height": 2.5,
    "roll_width": 0.53, "roll_length": 2.0, "pattern_cm": 0,
    "drops": 8, "drop_len_m": 2.5, "pattern_m": 0.0,
    "strips_per_roll": 1, "rolls": 8,
}

GEOMETRY_CASES = (MASTER_BED_PLAIN53, BIG_FLOWER_WALL, EXACT_FIT, REMAINDER_ROUND_UP, SHORT_ROLL)


@pytest.fixture(params=GEOMETRY_CASES, ids=[c["name"] for c in GEOMETRY_CASES])
def geometry_case(request):
    """Every hand-written geometry case, one parameter at a time."""
    return request.param


@pytest.fixture
def master_bed_case():
    """主卧一圈 × 素色53 — the canonical plain-paper regression case."""
    return MASTER_BED_PLAIN53


@pytest.fixture
def big_flower_case():
    """大花匹配 × 大花64 — the pattern-match wall from the seed data."""
    return BIG_FLOWER_WALL
