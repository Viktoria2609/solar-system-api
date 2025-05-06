from flask import Blueprint, request, Response
from app.models.planet import Planet
from ..db import db
from .route_utilites import validate_model, create_model, get_models_with_filters

bp = Blueprint("planet_list_bp", __name__, url_prefix = "/planet_list")


@bp.post("")
def create_planet():
    request_body = request.get_json()

    return create_model(Planet, request_body)

@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)

@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

@bp.put("/<planet_id>") 
def update_planet(planet_id):        
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.rings = request_body["rings"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
