from sqlalchemy import TEXT, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.core import Base


class Venue(Base):
    __tablename__ = "venues"

    name: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(TEXT)
    capacity: Mapped[int]
