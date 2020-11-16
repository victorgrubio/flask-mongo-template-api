from marshmallow import Schema, fields

class ErrorResponse(Schema):
    error = fields.String(description="Error returned by the API")
