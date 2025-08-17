"""Category router mapping question categories to role contracts."""
from __future__ import annotations

from typing import Dict

_CONTRACTS: Dict[str, Dict[str, str]] = {
    "education": {"examiner": "Sun"},
}


def get_contract(category: str) -> Dict[str, str]:
    """Return role contract for a given category (case-insensitive)."""
    if not category:
        return {}
    return _CONTRACTS.get(category.lower(), {})
