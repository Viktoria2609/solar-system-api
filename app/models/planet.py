from sqlalchemy.orm import Mapped, mapped_column, relationship
from  sqlalchemy import ForeignKey
from ..db import db
from typing import Optional


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    rings: Mapped[bool]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moon.id"))
    moon: Mapped[Optional["Moon"]] = relationship(back_populates="planets")


    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "rings": self.rings,
        "moon": self.moon.name if self.moon_id else None
        }

    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"],
            description = planet_data["description"],
            rings = planet_data["rings"],
            moon_id=planet_data.get("moon_id", None)
        )
