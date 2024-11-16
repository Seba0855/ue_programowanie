"""
5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list, a drugi
typu int. Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
drugim.
"""


def contains(values: list, value) -> bool:
    return value in values


test_values = ["Grzegorz", 3, 12.12, 'A', True]
print(contains(test_values, 'A'))
