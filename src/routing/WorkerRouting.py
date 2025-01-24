from http import HTTPStatus

from flask import json, Response
from flask_restful import Resource

from src.queue.common import find_work_by_id

class WorkerRouting(Resource):
    """ Route for accessing work statuses """

    def get(self, work_id: int) -> Response:
        work = find_work_by_id(work_id)
        if work is None:
            error = json.dumps({"error": f"Could not find worker with id {work_id}"})
            return Response(error, HTTPStatus.NOT_FOUND)

        result = json.dumps(work)
        return Response(result, HTTPStatus.OK)
