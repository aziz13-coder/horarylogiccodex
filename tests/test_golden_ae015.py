import json
from pathlib import Path

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.evaluate_chart import evaluate_chart
from backend.horary_engine.polarity_weights import TestimonyKey


def test_ae015_golden_expect_yes():
    data_path = Path(__file__).resolve().parent.parent / "backend" / "e AE-015 – “Will I pass my physiotherapy exam.json"
    chart = json.loads(data_path.read_text(encoding="utf-8"))
    result = evaluate_chart(chart)
    assert result["verdict"] == "YES"
    keys = [entry["key"] for entry in result["ledger"]]
    assert TestimonyKey.MOON_APPLYING_TRINE_EXAMINER_SUN in keys
