from flask import Flask
from flask_restful import Api
from src.routing.DetectionRouting import PeopleDetection
from src.routing.WorkerRouting import WorkerRouting

app = Flask(__name__)
api = Api(app)

api.add_resource(PeopleDetection, "/analyze_img")
api.add_resource(WorkerRouting, '/jobs/<int:work_id>')

## TODO: Refactor
if __name__ == "__main__":
    print("Starting server")
    app.run(debug=True)
