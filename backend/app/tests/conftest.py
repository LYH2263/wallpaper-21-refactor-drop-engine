"""共享几何夹具：与 seed.py 实体同源，另附两组手写几何。

夹具直接给几何包用，不经过 HTTP / 数据库。
"""

import pytest


@pytest.fixture
def big_pattern_wall():
    """seed.py 的「大花匹配」墙配「大花64」卷。"""
    return {
        "perimeter": 20.0,
        "height": 2.8,
        "roll_width": 0.53,
        "roll_length": 10.0,
        "pattern_cm": 64,
        "expect": {
            "drops": 38,
            "pattern_m": 0.64,
            "drop_len": 3.44,
            "strips_per_roll": 2,
            "rolls": 19,
        },
    }


@pytest.fixture
def plain_master_bed_geometry():
    """手写几何 1：主卧一圈配素色53（无花高）。"""
    return {
        "perimeter": 16.0,
        "height": 2.7,
        "roll_width": 0.53,
        "roll_length": 10.0,
        "pattern_cm": 0,
        "expect": {
            "drops": 31,
            "pattern_m": 0.0,
            "drop_len": 2.7,
            "strips_per_roll": 3,
            "rolls": 11,
        },
    }


@pytest.fixture
def short_wall_geometry():
    """手写几何 2：4m 小墙、窄卷、带 32cm 花距。"""
    return {
        "perimeter": 4.0,
        "height": 2.5,
        "roll_width": 0.5,
        "roll_length": 10.0,
        "pattern_cm": 32,
        "expect": {
            "drops": 8,          # 4.0 / 0.5
            "pattern_m": 0.32,
            "drop_len": 2.82,    # 2.5 + 0.32
            "strips_per_roll": 3,  # floor(10 / 2.82) = 3
            "rolls": 3,          # ceil(8 / 3)
        },
    }
