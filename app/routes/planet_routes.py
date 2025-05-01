from flask import Blueprint, request, Response
from app.models.planet import Planet
from ..db import db
from .route_utilites import validate_model

planet_list_bp = Blueprint("planet_list_bp", __name__, url_prefix = "/planet_list")


@planet_list_bp.post("")
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@planet_list_bp.get("")
def get_all_planets():

    query = db.select(Planet)
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    rings_param = request.args.get("rings")
    if rings_param is not None:
        if rings_param.lower() == "true":
            rings_bool = True
        elif rings_param.lower() == "false":
            rings_bool = False
        else:
            return {"error": "Invalid value for rings. Use true or false."}, 400

        query = query.where(Planet.rings == rings_bool)

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        print(planet, type(planet))
        planets_response.append(planet.to_dict())
    return planets_response

@planet_list_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

@planet_list_bp.put("/<planet_id>") 
def update_planet(planet_id):        
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.rings = request_body["rings"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planet_list_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
