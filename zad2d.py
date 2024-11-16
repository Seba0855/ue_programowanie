"""
Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
drugi element.
"""


def show_second_number(numbers):
    [print(numbers[index]) for index in range(len(numbers)) if index % 2 == 0]


numbers_range = range(9, 19)
show_second_number(numbers_range)
