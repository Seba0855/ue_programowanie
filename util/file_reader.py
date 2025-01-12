import json
import csv
from model.Movie import Movie


def read_data(filename: str):
    with open(filename, "r") as file:
        output = json.load(file)
    return [Movie(entry) for entry in output]


def read_csv(filename: str):
    with open(filename, "r") as file:
        csv_dict = csv.DictReader(file)
        return [entry for entry in csv_dict]


def serialize_items(items: list, object):
    return [object(entry) for entry in items]
