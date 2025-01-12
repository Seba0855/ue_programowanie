from flask_restful import Resource

from model.Movie import Movie
from model.Rating import Rating
from model.Link import Link
from model.Tag import Tag
from util.file_reader import read_csv, serialize_items


class MoviesRoute(Resource):
    def get(self):
        movies = read_csv("./data/movies.csv")
        return serialize_items(items=movies, object=Movie)


class LinksRoute(Resource):
    def get(self):
        links = read_csv("./data/links.csv")
        return serialize_items(items=links, object=Link)


class RatingsRoute(Resource):
    def get(self):
        ratings = read_csv("./data/ratings.csv")
        return serialize_items(items=ratings, object=Rating)


class TagsRoute(Resource):
    def get(self):
        tags = read_csv("./data/tags.csv")
        return serialize_items(items=tags, object=Tag)
