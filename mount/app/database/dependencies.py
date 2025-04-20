from typing import Annotated
from fastapi import Depends, Request, Query
from app.database.core import get_db_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from pydantic import BaseModel, Field

class PaginationParams(BaseModel):
    page: int = Field(..., description="Page number")
    per_page: int = Field(10, description="Number of itmes to show per page")


async def async_get_db(request: Request):
    async with AsyncSession(request.app.state.db_pool) as db:
        yield db


PaginationParamsDep = Annotated[PaginationParams, Query()]

AsyncSessionDep = Annotated[AsyncSession, Depends(async_get_db)]
