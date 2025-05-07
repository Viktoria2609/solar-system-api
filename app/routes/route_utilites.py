from flask import abort,make_response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        response = {"message": f"{cls.__name__} id {model_id} is invalid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"{cls.__name__} with id {model_id} not found"}
        abort(make_response(response, 404))

    return model

def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except KeyError as e:
        response = {"message": f"Invalid request: missing {e.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_model)
    db.session.commit()
    
    return new_model.to_dict(), 201

def get_models_with_filters(cls, filters=None):
    query = db.select(cls)

    if filters:
        for attribute, value in filters.items():
            if hasattr(cls, attribute):
                column_attr = getattr(cls, attribute)
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False

                if isinstance(column_attr.type.python_type, type) and column_attr.type.python_type == str:
                    query = query.where(column_attr.ilike(f"%{value}%"))
                else:
                    query = query.where(column_attr == value)

    models = db.session.scalars(query.order_by(cls.id))
    return [model.to_dict() for model in models]
