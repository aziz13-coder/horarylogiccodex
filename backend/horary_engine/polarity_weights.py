"""Central repository for testimony polarity and weight tables."""

from __future__ import annotations

from enum import Enum

from .polarity import Polarity


class TestimonyKey(Enum):
    """Canonical keys for all supported testimony tokens."""

    MOON_APPLYING_TRINE_EXAMINER_SUN = "moon_applying_trine_examiner_sun"
    MOON_APPLYING_SQUARE_EXAMINER_SUN = "moon_applying_square_examiner_sun"


# Prevent pytest from collecting the enum as a test class
TestimonyKey.__test__ = False


POLARITY_TABLE: dict[TestimonyKey, Polarity] = {
    # Favorable Moon applying trine to the examiner (Sun in education questions)
    TestimonyKey.MOON_APPLYING_TRINE_EXAMINER_SUN: Polarity.POSITIVE,
    # Example negative testimony
    TestimonyKey.MOON_APPLYING_SQUARE_EXAMINER_SUN: Polarity.NEGATIVE,
}

WEIGHT_TABLE: dict[TestimonyKey, float] = {
    TestimonyKey.MOON_APPLYING_TRINE_EXAMINER_SUN: 1.0,
    TestimonyKey.MOON_APPLYING_SQUARE_EXAMINER_SUN: 1.0,
}

