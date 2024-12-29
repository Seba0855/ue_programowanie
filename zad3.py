class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Property(area={self.area}, rooms={self.rooms}," \
               f" price={self.price}, address={self.address})"


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"House(area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}, plot={self.plot})"


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"Flat(area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}, floor={self.floor})"


if __name__ == "__main__":
    house = House(123.4, 4, 1923000, "Siemianowice ul. Bańgowska 44", 3)
    flat = Flat(42, 3, 599999999, "Katowice ul. Bogucicka 42/4", 4)

    print(house)
    print(flat)
