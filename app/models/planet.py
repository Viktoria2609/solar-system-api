class Planet:
    def __init__(self, id, name, description, rings):
        self.id = id
        self.name = name
        self.description = description
        self.rings = rings

planet_list = [
    Planet(1, "Mercury", "The smallest planet.", False),
    Planet(2, "Venus", "The hot planet.", False),
    Planet(3, "Earth", "Our home planet.", False),
    Planet(4, "Mars", "The red planet.", False),
    Planet(5, "Jupiter", "The largest planet in the solar system.", True),
    Planet(6, "Saturn", "The planet with prominent ring system.", True),
    Planet(7, "Uranus", "The ice giant planet.", True),
    Planet(8, "Neptune", "The distant planet.", True)
]