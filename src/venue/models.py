from typing import TYPE_CHECKING
from pydantic import BaseModel, Field
from sqlalchemy import TEXT, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.core import Base
from src.models import DBBaseModel

if TYPE_CHECKING:
    from src.concert.models import Concert


class Venue(Base):
    __tablename__ = "venues"

    name: Mapped[str] = mapped_column(String(255))
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
