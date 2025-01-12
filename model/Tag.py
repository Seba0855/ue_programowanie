from dataclasses import dataclass


@dataclass
class Tag:
    userId: int
    movieId: int
    tag: str
    timestamp: int
