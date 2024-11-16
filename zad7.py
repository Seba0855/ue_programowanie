import requests
from dataclasses import dataclass

"""
7. Stworzyć skrypt pythonowy, który połączy się z API, które zawiera informacje
o browarach (dokumentacja https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę
Brewery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
odpowiednim typowaniem.
W klasie należy zaimplementować magiczną metodę
__str__ która będzie opisywała dane przechowywane w obiekcie.
Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
utworzyć listę 20 instancji klasy
Brewery , którą przeiteruje i wyświetli każdy obiekt z osobna.
"""


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: str
    address_2: str
    address_3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float
    latitude: float
    phone: str
    website_url: str
    state: str
    street: str

    def __init__(self, input_json):
        self.__dict__ = input_json

    def __str__(self):
        return f"Napój bogów {self.name} wyprodukowany w {self.street}, {self.postal_code} {self.city}. Wejdź na {self.website_url} by dowiedzieć się więcej."


api_output = requests.get("https://api.openbrewerydb.org/v1/breweries")
breweries = [Brewery(output) for output in api_output.json()]

[print(brewery) for brewery in breweries]
