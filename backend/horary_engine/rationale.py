"""Utilities for turning a contribution ledger into human-readable text."""
from __future__ import annotations

from typing import List, Dict


def build_rationale(ledger: List[Dict[str, float | str]]) -> List[str]:
    """Create a rationale list from a contribution ledger.

    The function is pure and does not mutate the input ledger.
    """
    result: List[str] = []
    for entry in ledger:
        key = entry.get("key", "")
        weight = entry.get("weight", 0.0)
        polarity = entry.get("polarity", 0)
        sign = "+" if polarity >= 0 else "-"
        result.append(f"{key} {sign}{weight}")
    return result
