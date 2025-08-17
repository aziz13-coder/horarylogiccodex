"""Utilities for turning a contribution ledger into human-readable text."""
from __future__ import annotations

from typing import List, Dict

from .polarity_weights import Polarity, TestimonyKey
from .utils import token_to_string


def build_rationale(
    ledger: List[Dict[str, float | TestimonyKey | Polarity]]
) -> List[str]:
    """Create a rationale list from a contribution ledger.

    The function is pure and does not mutate the input ledger.
    """
    result: List[str] = []
    for entry in ledger:
        key = token_to_string(entry.get("key", ""))
        weight = entry.get("weight", 0.0)
        polarity = entry.get("polarity", Polarity.NEUTRAL)
        if polarity is Polarity.FAVORABLE:
            sign = "+"
        elif polarity is Polarity.UNFAVORABLE:
            sign = "-"
        else:
            sign = ""
        result.append(f"{key} {sign}{weight}")
    return result
