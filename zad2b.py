"""
b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
    dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
    zwróci. Zadanie należy wykonać w 2 wersjach:
    i. Wykorzystując pętle for .
    ii. Wykorzystując listę składaną.
"""


def multiply_numbers(numbers):
    output = []
    for number in numbers:
        output.append(number * 2)
    return output


def multiply_numbers_expr(numbers):
    return [number * 2 for number in numbers]


dataset = [9, 12, 512, 3, 8]
print(f"1 wersja: {multiply_numbers(dataset)}")
print(f"2 wersja: {multiply_numbers_expr(dataset)}")