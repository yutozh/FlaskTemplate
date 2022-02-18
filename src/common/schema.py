from marshmallow import Schema, ValidationError, fields, validates
from common.http.response import JsonResponse
from common.http.rc import RC
import typing
from dynaconf import settings

default_page_size = settings.get('default_page_size', 10)
max_page_size = settings.get('max_page_size', 50)


class BaseSchema(Schema):

    def handle_error(
            self, error: ValidationError, data: typing.Any, *, many: bool, **kwargs
    ):
        response = JsonResponse(rc=RC.invalid.value, message=list(error.messages.values())[0][0], error=error.messages)
        raise ValidationError(response)


class QuerySchema(BaseSchema):
    keywords = fields.String(required=False, missing='')
    page_no = fields.Integer(load_only=True, default=1, missing=1)
    page_size = fields.Integer(load_only=True, default=default_page_size, missing=default_page_size)

    @validates('page_no')
    def valid_page_no(self, value):
        if value <= 0:
            raise ValidationError('非法页码')
    
    @validates('page_size')
    def valid_page_size(self, value):
        if value > max_page_size:
            raise ValidationError('每页不超过50')