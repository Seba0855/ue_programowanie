from flask import Flask
from flask_restful import Api, Resource

from src.routing.DetectionRouting import PeopleDetection

"""
3 API posiada 1 endpoint GET, który odczytuje zdjęcie z dysku i zwrac
liczbę wykrytych osób.

4 API posiada 2 endpoiny, ten na 3
endpoint GET, który przyjmuje url do zdjęcia znajdującego się w
Internecie, endpoint zwraca liczbę osób wykrytych na tym zdjęciu,
oba endpointy zapisują prace na kolejce i wykonują ją w sposób
asynchroniczny,
oba endpointy w response zwracają ID zadania,
istnieje dodatkowy endpoint do weryfikacji statusu zadania i ewentualnego
wyniku z liczbą osób wykrytych na zdjęciu.

5 API posiada 3 endpoiny, te na 4
endpoint POST, do którego można przesłać zdjęcie, które zostanie
przeanalizowane,
endpoint zapisuje zadanie na kolejce i zwraca w response ID zadania.
"""

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, "/hello")
api.add_resource(PeopleDetection, "/analyze_img")

if __name__ == "__main__":
    print("Starting server")
    app.run(debug=True)
