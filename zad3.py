"""
3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
tekst "Liczba parzysta" / "Liczba nieparzysta"
"""


def is_even(number: int) -> bool:
    return number % 2 == 0


output = is_even(43)
print("Liczba parzysta" if output else "Liczba nieparzysta")
