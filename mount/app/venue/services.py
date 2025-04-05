from typing import cast
from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.ext import paginate
from app.venue.models import Venue, VenueCreateRequest


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
