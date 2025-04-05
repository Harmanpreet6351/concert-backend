from sqlalchemy.ext.asyncio import AsyncSession

from app.venue.models import Venue, VenueCreateRequest
from app.database.operations import QueryExecutor


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
    db: AsyncSession, page: int = 1, per_page: int = 10
) -> dict:
    """Get all venues in paginated form

    Args:
        db (AsyncSession): Async DB Session
        page (int, optional): Current Page. Defaults to 1.
        per_page (int, optional): Number of Items to show in a page. Defaults to 10.

    Returns:
        dict: Dictionary with Paginated Data
    """
    data = await QueryExecutor[Venue](Venue).paginate(
        db, pagination_data={"page": page, "per_page": per_page}
    )

    return data
