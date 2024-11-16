"""
4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
informację jako typ logiczny bool
"""


def sum_greater_than_number_3(number1: int, number2: int, number3: int) -> bool:
    return (number1 + number2) >= number3


print(sum_greater_than_number_3(43, 12, 50))
