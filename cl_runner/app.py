from flask import Flask
from flask_restx import Api, Resource
import requests

# app = Flask(__name__)

# @app.route("/cl_runner", methods=["GET"])
app = Flask(__name__)

# Initialize the Flask-RESTx API
api = Api(app, title="Runner Service", description="API documentation for the Runner Service", version="1.0")

# Define a namespace for grouping endpoints
ns = api.namespace("cl_runner", description="Clustering runner")

# Define the endpoint and its documentation
@ns.route("/cl_runner")
class Cluster_runner(Resource):
    def get(self):
        response = requests.get("http://cl_service:5001/cl_service/cl_service")
    # resp = response.json().get("message", "")
    # return jsonify({"message": f"{greeting} World"})
    # return response + "CL_RUNNER CALLED"
        return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)