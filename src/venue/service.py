from typing import cast
from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.ext import paginate
from src.venue.models import Venue, VenueCreateRequest


async def create_venue(db: AsyncSession, data: VenueCreateRequest) -> Venue:
    """Create a Venue to organize a concert

    Args:
        db (AsyncSession): Asynchronous Sqlalchemy DB Session obj
        data (VenueCreateRequest): Pydantic model object for create venu

    Returns:
        Venue: Venue model object
    """
    obj = Venue(**data.model_dump())

    db.add(obj)

    await db.commit()
    await db.refresh(obj)

    return obj


async def get_venues_paginated(
    db: AsyncSession, *, page: int = 1, per_page: int = 10
) -> dict[str, int | list[Venue]]:
    stmt = select(Venue)

    return await paginate(db, stmt)
