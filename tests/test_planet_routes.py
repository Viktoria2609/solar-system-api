def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planet_list")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planet_list/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pink Planet",
        "description": "very pink",
        "rings": False,
        "moon": None
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planet_list", json={
        "name": "New Planet",
        "description": "Unknown",
        "rings": False
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Planet",
        "description": "Unknown",
        "rings": False,
        "moon": None
    }