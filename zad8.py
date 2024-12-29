import requests
from dataclasses import dataclass

from zad7 import Brewery

"""
8. Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city , który może
być przekazywany w wierszu poleceń podczas wykonywania (np. python
main.py --city=Berlin ). Należy wykorzystać moduł argparse do wczytywania
przekazywanych parametrów, a w razie przekazania wartości ograniczyć
pobierane browary do miasta, które zostało wskazane.
"""


api_output = requests.get("https://api.openbrewerydb.org/v1/breweries")
breweries = [Brewery(output) for output in api_output.json()]

[print(brewery) for brewery in breweries]
