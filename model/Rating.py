from dataclasses import dataclass


@dataclass
class Ratings:
    userId: int
    movieId: int
    rating: float
    timestamp: int
