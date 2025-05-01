from sqlalchemy.orm import Mapped, mapped_column
from ..db import db


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    rings: Mapped[bool]


    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "rings": self.rings
        }

    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"],
            description = planet_data["description"],
            rings = planet_data["rings"]
        )
