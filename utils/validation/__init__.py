from flask import jsonify, request


def required_fields_exception(required_fields):
    def main_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                data = request.json
            except Exception:
                data = []
            error = {}
            for field in required_fields:
                if field not in data:
                    error[field] = "This Field Is Required"
            if error:
                return jsonify(error), 400
            else:
                return func(*args, **kwargs)

        return wrapper

    return main_decorator
