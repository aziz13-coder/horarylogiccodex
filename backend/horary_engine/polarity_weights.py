"""Central repository for testimony polarity and weight tables."""

POLARITY_TABLE = {
    # Favorable Moon applying trine to the examiner (Sun in education questions)
    "moon_applying_trine_examiner_sun": 1,
    # Example negative testimony
    "moon_applying_square_examiner_sun": -1,
}

WEIGHT_TABLE = {
    "moon_applying_trine_examiner_sun": 1.0,
    "moon_applying_square_examiner_sun": 1.0,
}
