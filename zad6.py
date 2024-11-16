"""
6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.
"""


def list_operations(list_values1: list, list_values2: list) -> list:
    return [num ** 3 for num in set(list_values1 + list_values2)]


test_values = [5, 3, 12.12, 3, 2]
test_values2 = [5, 10, 15, 9, 64]
print(list_operations(test_values, test_values2))
