from fastapi import APIRouter

from src.dependencies import AsyncSessionDep
from src.venue.models import PaginatedVenueRead, VenueCreateRequest, VenueRead
from src.venue.service import get_venues_paginated, create_venue as create_venue_db


venue_router = APIRouter(tags=["Venues"])


@venue_router.post("/venues", response_model=VenueRead)
async def create_venue(db: AsyncSessionDep, data: VenueCreateRequest):
    return await create_venue_db(db, data)


@venue_router.get("/venues", response_model=PaginatedVenueRead)
async def get_paginated_venues(db: AsyncSessionDep):
    return await get_venues_paginated(db)
