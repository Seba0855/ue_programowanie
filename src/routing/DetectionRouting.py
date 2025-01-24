from http import HTTPStatus

from flask import request, json, Response
from flask_restful import reqparse, Resource

from src.model.InputType import InputType
from src.queue.producer import enqueue_job


def schedule_work(job_type: InputType, content: str) -> int:
    job = enqueue_job(job_type, content)
    return job.id


class PeopleDetection(Resource):
    def __init__(self):
        self.parser = self.create_request_parser()

    def get(self):
        path = request.args.get('path')
        url = request.args.get('url')

        if not any((path, url)):
            error = json.dumps({"error": "You need to provide either image path or url"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        if all((path, url)):
            error = json.dumps({"error": "You should provide only image path or url"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        if url is None and path is not None:
            if path == '':
                error = json.dumps({"error": "You need to specify a valid path to file"})
                return Response(error, HTTPStatus.BAD_REQUEST)
            if path.__contains__("\"") or path.__contains__("\'"):
                error = json.dumps({"error": "Provide a relative path without parentheses"})
                return Response(error, HTTPStatus.BAD_REQUEST)

        if path is None and url is not None:
            if path == '':
                error = json.dumps({"error": "You need to specify a valid url containing file"})
                return Response(error, HTTPStatus.BAD_REQUEST)

        input_type = InputType.PATH if path is not None else InputType.URL
        analyzed_content = path if path is not None else url
        print(f"Scheduling {input_type} with content: {analyzed_content}")
        job_id = schedule_work(input_type, analyzed_content)

        return Response(json.dumps(job_id), HTTPStatus.ACCEPTED)

    def post(self) -> Response:
        ns = self.parser.parse_args()
        b64_img = ns.get("image")

        job_id = schedule_work(InputType.BASE64, b64_img)

        return Response(json.dumps(job_id), HTTPStatus.ACCEPTED)

    @staticmethod
    def create_request_parser() -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("image")
        return parser
