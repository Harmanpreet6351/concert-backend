from typing import TYPE_CHECKING
from pydantic import BaseModel
from sqlalchemy import TEXT, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.core import Base
from app.database.models import DBBaseModel

if TYPE_CHECKING:
    from app.concert.models import Concert


class Venue(Base):
    __tablename__ = "venues"

    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(TEXT)
    capacity: Mapped[int]

    # Relationships
    concerts: Mapped[list["Concert"]] = relationship(back_populates="venue")


class VenueRead(DBBaseModel):
    name: str
    location: str
    capacity: int


class VenueCreateRequest(BaseModel):
    name: str
    location: str
    capacity: str
