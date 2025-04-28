from flask import abort, make_response, Blueprint, request, Response
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

    query = db.select(Planet)#(query.order_by(Planet.id))
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    query = query.order_by(Planet.id)
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

@planet_list_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "rings": planet.rings
    }

@planet_list_bp.put("/<planet_id>") 
def update_planet(planet_id):        
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.rings = request_body["rings"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = {"message": f"Planet {planet_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"Planet {planet_id} not found"}
        abort(make_response(response, 404))

    return planet

@planet_list_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
