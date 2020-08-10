from schematics import Model
from schematics.exceptions import DataError
from flask import jsonify, request
from functools import wraps


def validate_schema(schema_in: 'Model'):
    def validate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                partial = request.method.lower() == 'patch'

                schema_obj = schema_in(request.json)
                schema_obj.validate(partial=partial)

                return fn(*args, **kwargs)
            except DataError as e:
                response = jsonify(e.to_primitive())
                response.status_code = 422
                return response

        return wrapper

    return validate
