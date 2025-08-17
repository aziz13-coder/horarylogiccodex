"""Aggregate testimonies into a score with a contribution ledger."""
from __future__ import annotations

from typing import Iterable, List, Tuple, Dict

from .polarity_weights import POLARITY_TABLE, WEIGHT_TABLE


def aggregate(testimonies: Iterable[str]) -> Tuple[float, List[Dict[str, float | str]]]:
    """Aggregate testimony tokens into a weighted score and ledger.

    The aggregator is *symmetric* in that positive and negative testimonies are
    treated uniformly via the ``POLARITY_TABLE``. It enforces several
    invariants:

    * polarity: each token must map to -1 or +1
    * monotonicity: weights are non-negative and contributions sum linearly
    * single contribution: duplicate tokens are ignored
    * deterministic order: processing occurs in sorted token order
    """

    total_yes = 0.0
    total_no = 0.0
    ledger: List[Dict[str, float | str]] = []
    seen: set[str] = set()

    for token in sorted(testimonies):
        if token in seen:
            continue
        seen.add(token)
        polarity = POLARITY_TABLE.get(token)
        if polarity not in (-1, 1):
            continue  # unknown or neutral token
        weight = WEIGHT_TABLE.get(token, 0.0)
        if weight < 0:
            raise ValueError("Weights must be non-negative for monotonicity")
        delta_yes = weight if polarity > 0 else 0.0
        delta_no = weight if polarity < 0 else 0.0
        total_yes += delta_yes
        total_no += delta_no
        ledger.append({
            "key": token,
            "polarity": polarity,
            "weight": weight,
            "delta_yes": delta_yes,
            "delta_no": delta_no,
        })

    total = total_yes - total_no
    return total, ledger
