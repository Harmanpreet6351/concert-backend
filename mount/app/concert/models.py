from datetime import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel, Field
from sqlalchemy import TIMESTAMP, ForeignKey, Numeric, String
from app.database.core import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import DBBaseModel
from app.venue.models import VenueRead

if TYPE_CHECKING:
    from app.venue.models import Venue


class Concert(Base):
    __tablename__ = "concerts"

    title: Mapped[str] = mapped_column(String)
    artist: Mapped[str] = mapped_column(String)
    venue_id: Mapped[int | None] = mapped_column(
        ForeignKey("venues.id", name="concert_venue_fk")
    )
    event_date: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    ticket_price: Mapped[float | None] = mapped_column(Numeric(10, 2, asdecimal=False))

    venue: Mapped["Venue | None"] = relationship(foreign_keys=[venue_id])


class ConcertRead(DBBaseModel):
    title: str
    artist: str
    event_date: datetime | None
    ticket_price: float | None

    venue: VenueRead | None


class ConcertCreate(BaseModel):
    title: str = Field(..., examples=["Melodisa 6"])
    artist: str = Field(..., examples=["Justin Beiber"])
    event_date: datetime | None = Field(..., examples=[datetime(2025, 5, 2, 3, 2, 1)])
    ticket_price: float | None = Field(..., examples=[7.4])
