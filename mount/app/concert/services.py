from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.concert.models import Concert
from app.database.operations import QueryDB
from app.venue.models import Venue


async def add_concert_to_venue(
    db: AsyncSession, concert_id: int, venue_id: int
) -> Concert:
    concert_obj = await QueryDB[Concert](
        Concert, filter_spec=[("id", "eq", concert_id)]
    ).get_one_or_404(db)

    venue_obj = await QueryDB[Venue](
        Venue, filter_spec=[("id", "eq", venue_id)]
    ).get_one_or_404(db)

    concert_obj.venue = venue_obj

    await db.commit()
    await db.refresh(concert_obj)

    return concert_obj
