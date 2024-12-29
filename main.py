from model.zad2 import *
from model.zad3 import House, Flat

if __name__ == "__main__":
    # Zad 1
    s1 = Student("Dawid Cyganek", [30.5, 50, 67, 83.5])
    s2 = Student("Jan Nowak", [95.5, 10, 25.5, 15])

    print("Printing results for ex 1")
    print(f"s1.is_passed() = {s1.is_passed()}")
    print(f"s2.is_passed() = {s2.is_passed()}\n")

    # Zad 2
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

    print("Printing results for ex 2")
    print(o1)
    print(o2, "\n")

    # Zad 3
    house = House(123.4, 4, 1923000, "Siemianowice ul. Bańgowska 44", 3)
    flat = Flat(42, 3, 599999999, "Katowice ul. Bogucicka 42/4", 4)

    print("Printing results for ex 3")
    print(house)
    print(flat, "\n")
