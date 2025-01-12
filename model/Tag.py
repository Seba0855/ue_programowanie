from dataclasses import dataclass


@dataclass
class Tag:
    userId: int
    movieId: int
    tag: str
    timestamp: int

    def __init__(self, input_json):
        self.__dict__ = input_json

    def __str__(self):
        return f"{self.__dict__}"
