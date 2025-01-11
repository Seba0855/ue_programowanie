import json
from model.Movie import Movie


def read_data(filename: str):
    with open(filename, "r") as file:
        output = json.load(file)
    return [Movie(entry) for entry in output]
