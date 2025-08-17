from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.horary_engine.aggregator import aggregate

POS = "moon_applying_trine_examiner_sun"
NEG = "moon_applying_square_examiner_sun"


def test_polars_and_monotonicity():
    score_pos, ledger_pos = aggregate([POS])
    assert score_pos > 0
    entry_pos = ledger_pos[0]
    assert entry_pos["key"] == POS
    assert entry_pos["delta_yes"] > 0 and entry_pos["delta_no"] == 0
    # Duplicate contributions do not increase score
    score_dup, _ = aggregate([POS, POS])
    assert score_dup == score_pos

    score_both, _ = aggregate([POS, NEG])
    assert score_both < score_pos

    score_neg, ledger_neg = aggregate([NEG])
    assert score_neg < 0
    entry_neg = ledger_neg[0]
    assert entry_neg["delta_no"] > 0 and entry_neg["delta_yes"] == 0
