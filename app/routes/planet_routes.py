from flask import Blueprint
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

