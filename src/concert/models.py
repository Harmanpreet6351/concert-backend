



from datetime import datetime
from sqlalchemy import TIMESTAMP, ForeignKey, Numeric, String
from src.database.core import Base

from sqlalchemy.orm import Mapped, mapped_column


class Concert(Base):

    __tablename__ = "concerts"

    title: Mapped[str] = mapped_column(String(255))
    artist: Mapped[str] = mapped_column(String(255))
    venue_id: Mapped[int | None] = mapped_column(ForeignKey("venues.id", name="concert_venue_fk"))
    event_date: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    ticket_price: Mapped[float | None] = mapped_column(Numeric(10,2, asdecimal=False))
