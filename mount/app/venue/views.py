from fastapi import APIRouter

from app.database.dependencies import AsyncSessionDep, PaginationParamsDep
from app.models import PaginatedResponse
from app.venue.models import VenueCreateRequest, VenueRead

import app.venue.services as venue_service

venue_router = APIRouter(tags=["Venues"])


@venue_router.post("/venues", response_model=VenueRead)
async def create_venue(db: AsyncSessionDep, data: VenueCreateRequest):
    return await venue_service.create_venue(db, data)


@venue_router.get("/venues", response_model=PaginatedResponse[VenueRead])
async def get_paginated_venues(db: AsyncSessionDep, page_data: PaginationParamsDep):
    return await venue_service.get_venues_paginated(
        db, page=page_data.page, per_page=page_data.per_page
    )
