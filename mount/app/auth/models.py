from datetime import datetime, timedelta, timezone
import bcrypt
from pydantic import BaseModel, ConfigDict
from sqlalchemy import String
from app.config import get_settings
from app.database.core import Base
from sqlalchemy.orm import Mapped, mapped_column
from jose import jwt

from app.database.models import DBBaseModel


class User(Base):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    password_hash: Mapped[str] = mapped_column(String)

    @property
    def token(self) -> str:

        payload = {
            "sub": str(self.id),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        }

        return jwt.encode(
            payload,
            get_settings().secret_key,
        )

    def set_password(self, password: str) -> None:
        pw = password.encode()
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(pw, salt).decode()

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())


class UserRead(DBBaseModel):
    full_name: str
    email: str
    password_hash: str


class UserCreateRequest(BaseModel):
    full_name: str
    email: str
    password: str


class TokenResponse(BaseModel):
    token: str
    user: UserRead

    model_config = ConfigDict(from_attributes=True)
