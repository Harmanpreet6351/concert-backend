from typing import Annotated

from fastapi import Depends
from src.database.core import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession


async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db


AsyncDBSession = Annotated[AsyncSession, Depends(async_get_db)]
