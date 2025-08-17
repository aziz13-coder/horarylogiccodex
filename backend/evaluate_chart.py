"""Evaluation pipeline orchestrating testimony extraction and aggregation."""
from __future__ import annotations

import logging
from typing import Any, Dict

from backend.category_router import get_contract
from backend.horary_engine.engine import extract_testimonies
from backend.horary_engine.aggregator import aggregate
from backend.horary_engine.rationale import build_rationale

logger = logging.getLogger(__name__)


def evaluate_chart(chart: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate a horary chart and return verdict with diagnostics.

    The function performs the following steps:

    1. Resolve the category contract (e.g., Sun as examiner for education).
    2. Extract normalized testimony tokens from the chart.
    3. Aggregate testimonies into a numeric score and contribution ledger.
    4. Build a human readable rationale from the ledger.
    """
    contract = get_contract(chart.get("category", ""))
    testimonies = extract_testimonies(chart, contract)
    score, ledger = aggregate(testimonies)
    logger.debug("Contribution ledger: %s", ledger)
    rationale = build_rationale(ledger)
    verdict = "YES" if score > 0 else "NO"
    return {"verdict": verdict, "ledger": ledger, "rationale": rationale}
