import mongoengine as me
import mongoengine_goodjson as me_json
from datetime import datetime

class Car(me_json.Document):
    model = me.StringField(description="Model of car")
    brand = me.StringField(description="Brand of car")
    year = me.IntField(description="Year of creation")

