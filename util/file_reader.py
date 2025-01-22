import csv


def read_csv(filename: str):
    with open(filename, "r") as file:
        csv_dict = csv.DictReader(file)
        return [entry for entry in csv_dict]


def serialize_items(items: list, object):
    return [object(entry).__dict__ for entry in items]
