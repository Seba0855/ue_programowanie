"""
Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli jedynie parzyste elementy.
"""


def show_even_numbers(numbers):
    [print(number) for number in numbers if number % 2 == 0]


numbers_range = range(1, 11)
show_even_numbers(numbers_range)
