from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
import json
import yaml
import schemas

from app import app as flask_app
import app

"""Create spec
"""
spec = APISpec(
    openapi_version="3.0.0",
    title="Health Weareable REST API",
    version='1.1.0',
    info={
        "description": "API Template using Flask and Mongo. The development of this service is provided by GATV, a research group from the Technical University of Madrid.",
        "termsOfService": "http://swagger.io/terms/",
        "contact": {
          "email": "vgr@gatv.ssr.upm.es"
        },
        "license": {
          "name": "Apache 2.0",
          "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
        }
    },
    servers = ["http://localhost:4000", "http://car_api:4000"],
    tags = [
        {
          "name": "car",
          "description": "Car related endpoints"
        }
    ],
    plugins=[MarshmallowPlugin(), FlaskPlugin()]
)


"""Definition of schemas
"""
# Data
spec.components.schema("CarSchema", schema=schemas.CarSchema)
spec.components.schema("ApiResponse", schema=schemas.ApiResponse)
spec.components.schema("ErrorResponse", schema=schemas.ErrorResponse)



"""Add methods from each route
"""
with flask_app.test_request_context():
    spec.path(view=app.add_new_car)
    spec.path(view=app.get_all_cars)


"""Save file in json and yaml
"""
with open(f'static/swagger.json', 'w') as json_file:
    json.dump(spec.to_dict(), json_file)

