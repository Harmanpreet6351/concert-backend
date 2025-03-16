from pydantic import BaseModel
from sqlalchemy import String
from src.database.core import Base
from sqlalchemy.orm import Mapped, mapped_column

from src.models import DBBaseModel


class User(Base):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))

    def set_password(self, password: str):
        # TODO: generate hash
        self.password_hash = password


class UserRead(DBBaseModel):
    full_name: str
    email: str
    password_hash: str


class UserCreateRequest(BaseModel):
    full_name: str
    email: str
    password: str
