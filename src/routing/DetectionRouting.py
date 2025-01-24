from http import HTTPStatus

from flask import request, json, Response
from flask_restful import reqparse, Api, Resource

from src.model.InputType import InputType
from src.util.person_detection import person_detection
from src.queue.producer import enqueue_job
from src.queue.common import find_job_by_id


class PeopleDetection(Resource):
    def __init__(self):
        self.parser = self.create_request_parser()

    def get(self):
        path = request.args.get('path')
        url = request.args.get("url")

        if not any((path, url)):
            error = json.dumps({"error": "You need to provide either image path or url"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        if all((path, url)):
            error = json.dumps({"error": "You should provide only image path or url"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        if path is None or path == '':
            error = json.dumps({"error": "You need to specify a path to file"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        if path.__contains__("\"") or path.__contains__("\'"):
            error = json.dumps({"error": "Provide a relative path without parentheses"})
            return Response(error, HTTPStatus.BAD_REQUEST)

        input_type = InputType.PATH if path is not None else InputType.URL
        analyzed_content = path if path is not None else url
        job_id = self.enqueue_job(input_type, analyzed_content)

        return Response(json.dumps(job_id), HTTPStatus.ACCEPTED)

    def post(self) -> Response:
        ns = self.parser.parse_args()
        content = ns.get("content")

        job_id = self.enqueue_job(InputType.BASE64, content)

        return Response(json.dumps(job_id), HTTPStatus.ACCEPTED)

    def enqueue_job(self, job_type: InputType, content: str) -> int:
        job = enqueue_job(job_type, content)
        return job.id

    @staticmethod
    def create_request_parser() -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("content")
        return parser


class JobsResource(Resource):
    """ API resource for quering job statuses. """

    def get(self, job_id: int) -> Response:
        job = find_job_by_id(job_id)
        if job is None:
            error = json.dumps({"error": f"job with id {job_id} does not exist"})
            return Response(error, HTTPStatus.NOT_FOUND)

        result = json.dumps(job)
        return Response(result, HTTPStatus.OK)
