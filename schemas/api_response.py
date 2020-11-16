from marshmallow import Schema, fields

class ApiResponse(Schema):
    status = fields.String(description="Status returned by the API")
