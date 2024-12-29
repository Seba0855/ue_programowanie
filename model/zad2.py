from typing import List
from model.zad1 import Student


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Library(city={self.city}, street={self.street}, zip_code={self.zip_code}, "
            f"opening_hours={self.open_hours}, phone_number={self.phone})"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Employee(first_name={self.first_name}, last_name={self.last_name}, hire_date={self.hire_date},"
            f" birth_date={self.birth_date}, city={self.city}, street={self.street}, "
            f"zip_code={self.zip_code}, phone_number={self.phone})"
        )


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"Book(library={str(self.library)}, publication_date={self.publication_date}, "
            f"author_name={self.author_name}, author_surname={self.author_surname}, "
            f"number_of_pages={self.number_of_pages})"
        )


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: List[Book], order_date: str
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books = f"[{', '.join(str(b) for b in self.books)}]"
        return (
            f"Order(employee={str(self.employee)}, student={self.student}, books={books}, "
            f"order_date={self.order_date})"
        )


if __name__ == "__main__":
    l1 = Library("Katowice", "Bankowa", "40-400", "8:00 - 16:00", "+48 636 343 636")
    l2 = Library("Siemianowice", "Śląska", "41-100", "6:00 - 20:00", "+48 997 998 999")

    b1 = Book(l1, "01.01.2020", "Paulina", "Drabczyk", 420)
    b2 = Book(l1, "02.02.2021", "Sebastian", "Matuszczyk", 1264)
    b3 = Book(l2, "03.03.2022", "Alicja", "Długosz", 178)
    b4 = Book(l2, "04.04.2023", "Agata", "Meble", 68)
    b5 = Book(l2, "05.05.2024", "Zbigniew", "Ilnicki", 239)

    e1 = Employee(
        "Jan",
        "Paweł",
        "02.04.2005",
        "14.01.1920",
        "Wadowice",
        "Kremówkowa",
        "45-440",
        "+48 666 555 444",
    )
    e2 = Employee(
        "Piotr",
        "Żyła",
        "4.11.2022",
        "17.01.2001",
        "Wisła",
        "Wiślańska",
        "53-123",
        "+48 111 222 333",
    )
    e3 = Employee(
        "Andrzej",
        "Dudu",
        "10.10.2010",
        "11.11.1954",
        "Warszawa",
        "Biały dom",
        "00-070",
        "+48 666 666 666",
    )

    s1 = Student("Jan Lipiński", [110, 92, 30, 40, 84.2])
    s2 = Student("Piotr Konieczny", [90.3, 34, 102, 32, 79.5])
    s3 = Student("Rafał Piech", [12, 43, 22, 9, 93])

    o1 = Order(e2, s1, [b2, b1], "15.12.2024")
    o2 = Order(e1, s2, [b5, b3, b4], "11.10.2024")

    print(o1)
    print(o2)
