



from typing import Literal
from pydantic import Field
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.core import Base
from app.models import DBBaseModel


TicketStatus = Literal[
    "available",
    "booked"
]

class Ticket(Base):

    __tablename__ = "tickets"

    concert_id: Mapped[int] = mapped_column(ForeignKey("concerts.id", name="ticket_concert_fk"))
    seat_number: Mapped[str | None] = mapped_column(String)
    status: Mapped[TicketStatus] = mapped_column(String)



class TicketRead(DBBaseModel):

    concert_id: int = Field(..., examples=[1,33,45])
    seat_number: str | None = Field(None, examples=["A23", "72", "61"])
    status: TicketStatus = Field("available", examples=["available", "booked"])