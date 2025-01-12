from dataclasses import dataclass


@dataclass
class Link:
    movieId: int
    imdbId: int
    tmdbId: int
