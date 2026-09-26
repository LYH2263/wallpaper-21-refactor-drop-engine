"""roll_count 串调测例: response field set and numbers against the fixtures."""

from app.engines.wallpaper_math import roll_count

EXPECTED_FIELDS = {"drops", "drop_len_m", "pattern_m", "strips_per_roll", "rolls"}


def _run(case):
    return roll_count(
        case["perimeter"], case["height"], case["roll_width"], case["roll_length"], case["pattern_cm"]
    )


def test_roll_count_matches_hand_fixtures(geometry_case):
    result = _run(geometry_case)
    assert set(result) == EXPECTED_FIELDS
    assert result == {
        "drops": geometry_case["drops"],
        "drop_len_m": geometry_case["drop_len_m"],
        "pattern_m": geometry_case["pattern_m"],
        "strips_per_roll": geometry_case["strips_per_roll"],
        "rolls": geometry_case["rolls"],
    }


def test_master_bed_plain53_numbers(master_bed_case):
    result = _run(master_bed_case)
    assert (result["drops"], result["strips_per_roll"], result["rolls"]) == (31, 3, 11)


def test_big_flower_wall_numbers(big_flower_case):
    result = _run(big_flower_case)
    assert (result["drops"], result["strips_per_roll"], result["rolls"]) == (38, 2, 19)
