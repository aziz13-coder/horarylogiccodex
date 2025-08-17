import json
from pathlib import Path

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.evaluate_chart import evaluate_chart


def test_ae015_golden_expect_yes():
    data_path = Path(__file__).resolve().parent.parent / "backend" / "e AE-015 – “Will I pass my physiotherapy exam.json"
    chart = json.loads(data_path.read_text(encoding="utf-8"))
    result = evaluate_chart(chart)
    assert result["verdict"] == "YES"
    keys = [entry["key"] for entry in result["ledger"]]
    assert "moon_applying_trine_examiner_sun" in keys
