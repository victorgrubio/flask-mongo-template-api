from flask import Response, jsonify, request
import traceback
from datetime import datetime, timedelta
import pytz
import jsonpickle
import logging
from models import Car
from schemas import ApiResponse, ErrorResponse

logger = logging.getLogger('gunicorn.error')

def add_new_car():
    """[summary]
    """
    try:
        car_data = request.get_json()
        db_data = Car(**car_data)
        db_data.save()
        response_pickled = jsonpickle.encode({"status": "Received"})
        return Response(response=response_pickled, status=200, mimetype="application/json")
    except Exception as e:
        logger.error(f"Error {e}")
        logger.error(traceback.print_exc())
        error_response = jsonpickle.encode({"error": "Internal Server Error"})
        return Response(response=error_response, status=500, mimetype="application/json")


def get_all_cars():
    """[summary]
    """
    try:
        return Car.objects().to_json()
    except Exception as e:
        logger.error(f"Error {e}")
        logger.error(traceback.print_exc())
        error_response = jsonpickle.encode({"error": "Internal Server Error"})
        return Response(response=error_response, status=500, mimetype="application/json")

