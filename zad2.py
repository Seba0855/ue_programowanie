from flask import Flask
from flask_restful import Resource, Api
from util.file_reader import read_data


app = Flask(__name__)
api = Api(app)


class Movies(Resource):
    def get(self):
        movies = read_data("./data/movies.json")
        return [movie.__dict__ for movie in movies]


api.add_resource(Movies, "/movies")

if __name__ == "__main__":
    app.run(debug=True)
