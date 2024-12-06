from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

# Initialize the Flask-RESTx API
api = Api(app, title="Clusterer Service", description="API documentation for the Clusterer Service", version="1.0")

# Define a namespace for grouping endpoints
ns = api.namespace("cl_service", description="Clustering operation")

# Define the endpoint and its documentation
@ns.route("/cl_service")
class Clusterer(Resource):
    def get(self):
        """Performs clusterization on a dataset with given parameters"""

        # return {"message": "clusterer"}
        return "CL_SERVICE CALLED"

# Add the namespace to the API
api.add_namespace(ns)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)