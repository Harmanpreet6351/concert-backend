from pydantic import BaseModel, Field
from sqlalchemy import TEXT, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.core import Base
from src.models import DBBaseModel


class Venue(Base):
    __tablename__ = "venues"

    name: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(TEXT)
    capacity: Mapped[int]


class VenueRead(DBBaseModel):
    name: str
    location: str
    capacity: int


class VenueCreateRequest(BaseModel):
    name: str
    location: str
    capacity: str


class PaginatedVenueRead(BaseModel):
    page: int
    total_pages: int
    data: list[VenueRead] = Field([])
