from flask import Flask, request
from flask_restful import Api

from endpoints.version import Version
from endpoints.math import circle, triangle

# Documentation on flask_restful
# https://flask-restful.readthedocs.io/en/latest/index.html

app = Flask(__name__)
api = Api(app)

"""Arguments can be passed to the constructor using the
parameters 'resource_class_args' and 'resource_class_kwargs'.

https://flask-restful.readthedocs.io/en/latest/api.html#flask_restful.Api.add_resource
"""

api.add_resource(Version, "/version",
                 resource_class_kwargs={"version": "1.0"})
api.add_resource(circle.Circumference, "/math/circle/circumference")
api.add_resource(circle.Radius, "/math/circle/radius")
api.add_resource(triangle.Area, "/math/triangle/area")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()