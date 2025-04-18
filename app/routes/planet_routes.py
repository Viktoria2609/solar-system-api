from flask import abort, make_response, Blueprint
from ..models.planet import planet_list


planet_list_bp = Blueprint("planet_list_bp", __name__, url_prefix = "/planet_list")

@planet_list_bp.get("")
def get_all_planets():
    result_list = []

    for planet in planet_list:
        result_list.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            rings = planet.rings
        ))
    return result_list

@planet_list_bp.get("/<id>")
def get_one_planet(id):
    print(f"Incoming ID: {id}")
    planet = validate_planet(id)

    planet_dict = dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            rings = planet.rings
            )
    return planet_dict

def validate_planet(id):
    try:
        id = int(id)
    except:
        response = {"message": f"Planet id {id} is invalid"}
        abort(make_response(response, 400))
    
    for planet in planet_list:
        if planet.id == id:
            return planet
        
    not_found = {"message": f"Planet with id ({id}) not found"}
    abort(make_response(not_found, 404))