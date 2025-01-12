from dataclasses import dataclass


@dataclass
class Link:
    movieId: int
    imdbId: int
    tmdbId: int

    def __init__(self, input_json):
        self.__dict__ = input_json

    def __str__(self):
        return f"{self.__dict__}"