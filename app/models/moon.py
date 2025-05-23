from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[int]
    planets: Mapped[list["Planet"]] = relationship(back_populates="moon")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }
        

    @classmethod
    def from_dict(cls, moon_data):
        new_moon = cls(
        name=moon_data["name"],
        description=moon_data["description"],
        size=moon_data["size"]
        )
        return new_moon