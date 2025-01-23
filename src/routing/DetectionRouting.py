from http import HTTPStatus

from flask import request, json, Response
from flask_restful import reqparse, Api, Resource
from src.util.person_detection import person_detection


class PeopleDetection(Resource):
    def __init__(self):
        self.parser = self.request_parser()

    def get(self):
        path = request.args.get('path')

        if path is None or path == '':
            error = json.dumps({"error": "You need to specify a path to file"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        if path.__contains__("\"") or path.__contains__("\'"):
            error = json.dumps({"error": "Provide a relative path without parentheses"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        detected_people = person_detection(path)
        result = json.dumps({"analyzed_file_path": path, "detected_people": detected_people})
        return Response(result, HTTPStatus.OK)

    @staticmethod
    def request_parser() -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("content")
        return parser
