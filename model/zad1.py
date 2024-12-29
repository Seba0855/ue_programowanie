from typing import List


class Student:
    def __init__(self, name: str, marks: List[float]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return (sum(self.marks) / len(self.marks)) > 50


if __name__ == "__main__":
    s1 = Student("Dawid Cyganek", [30.5, 50, 67, 83.5])
    s2 = Student("Jan Nowak", [95.5, 10, 25.5, 15])

    print(f"s1.is_passed() = {s1.is_passed()}")
    print(f"s2.is_passed() = {s2.is_passed()}")
