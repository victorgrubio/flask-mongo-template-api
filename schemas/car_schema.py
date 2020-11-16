from marshmallow import fields
from marshmallow_mongoengine import ModelSchema
import models

class CarSchema(ModelSchema):
    class Meta:
        model = models.Car
