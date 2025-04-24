from flask import abort, make_response, Blueprint, request
from app.models.planet import Planet
from ..db import db

planet_list_bp = Blueprint("planet_list_bp", __name__, url_prefix = "/planet_list")


@planet_list_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    rings = request_body["rings"]
    
    new_planet = Planet(name=name, description=description, rings=rings)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "rings": new_planet.rings
    }
    return response, 201

@planet_list_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "rings": planet.rings
                }
        )
    return planets_response
