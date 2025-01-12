from flask import Flask
from flask_restful import Api

from routing.HelloWorld import HelloWorld
from routing.MovieRoutes import *

app = Flask(__name__)
api = Api(app)

# zad 1
api.add_resource(HelloWorld, "/hello")

# zad 4
api.add_resource(MoviesRoute, "/movies")
api.add_resource(LinksRoute, "/links")
api.add_resource(TagsRoute, "/tags")
api.add_resource(RatingsRoute, "/ratings")

if __name__ == "__main__":
    print("Starting server")
    app.run(debug=True)
