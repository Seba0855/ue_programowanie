"""
a. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
wyświetli każde z nich.
"""


def print_names(names: list):
    for name in names:
        print(name)


name_list = ["Agata", "Dawid", "Sebastian", "Paulina", "Darek"]
print_names(name_list)
