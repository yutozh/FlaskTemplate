from marshmallow import Schema, fields, ValidationError, post_load, validates, pre_load, validates_schema
from sqlalchemy.orm import load_only
from common.schema import BaseSchema, QuerySchema

class HelloSchema(BaseSchema):
    pass