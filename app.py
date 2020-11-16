from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
import traceback
from datetime import datetime, timedelta
import pytz
import jsonpickle
import logging
from models import Car
from flask_swagger_ui import get_swaggerui_blueprint

import router


app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = MongoEngine(app)
# CORS(app, resources={r"/*": {"origins": "*"}})
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

# Register docs on API
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "GATV Car Template API"})
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/cars', methods=['POST'])
def add_new_car():
    """
    Add new car to DB
    ---
    post:
        tags: 
            - cars
        summary: Add new car to DB
        description: Send a new car and save it to the DB
        operationId: add_new_car
        requestBody:
            description: Car
            required: true
            content:
                application/json:
                    schema: CarSchema
        responses: 
            200:
                description: Car has been saved properly
                content:
                    application/json:
                        schema: ApiResponse
            500: 
                description: Internal server error
                content:
                    application/json:
                        schema: ErrorResponse
            default:
                description: Unexpected server response
                content:
                    application/json: 
                        schema: ErrorResponse 
    """
    app.logger.info(f'POST /car')
    return router.add_new_car()


@app.route('/cars', methods=['GET'])
def get_all_cars():
    """
    Get all cars from DB
    ---
    get:
        tags: 
            - cars
        summary:  Get all cars from DB
        description: Get all cars from DB
        operationId: get_all_cars
        responses: 
            200:
                description: Device data list
                content:
                    application/json:
                        schema: 
                            type: array
                            items:
                                schema: CarSchema 
            500: 
                description: Internal server error
                content:
                    application/json:
                        schema: ErrorResponse
            default:
                description: Unexpected server response
                content:
                    application/json: 
                        schema: ErrorResponse 
    """
    app.logger.info(f'GET /cars')
    return router.get_all_cars()


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=cfg.port)
