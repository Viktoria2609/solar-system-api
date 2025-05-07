from flask import Blueprint, request, Response
from app.models.moon import Moon
from app.models.planet import Planet
from .route_utilites import validate_model, create_model, get_models_with_filters
from app.models import planet
from ..db import db


bp = Blueprint("moon_bp", __name__, url_prefix="/moon")

@bp.post("")
def create_moon():
    request_body = request.get_json()
    
    return create_model(Moon, request_body)

@bp.post("/<id>/planet_list")
def create_planet_with_moon_id(id):
    moon = validate_model(Moon, id)
    request_body = request.get_json() 
    request_body ["moon_id"] = moon.id

    return create_model(Planet, request_body)


@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)


@bp.get("/<id>/planet_list")
def get_all_moons_planets(id):
    moon = validate_model(Moon, id)
    response = [planet.to_dict() for planet in moon.planets]
    
    return response
