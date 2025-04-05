from fastapi import APIRouter

from app.database.operations import db_get_item_by_filter_spec
from app.dependencies import AsyncSessionDep, PaginationParamsDep
from app.models import PaginatedResponse
from app.venue.models import Venue, VenueCreateRequest, VenueRead
from app.venue.services import create_venue as create_venue_db


venue_router = APIRouter(tags=["Venues"])


@venue_router.post("/venues", response_model=VenueRead)
async def create_venue(db: AsyncSessionDep, data: VenueCreateRequest):
    return await create_venue_db(db, data)


@venue_router.get("/venues", response_model=PaginatedResponse[VenueRead])
async def get_paginated_venues(db: AsyncSessionDep, page_data: PaginationParamsDep):
    return await db_get_item_by_filter_spec(
        db,
        Venue,
        pagination_data={"page": page_data.page, "per_page": page_data.per_page},
    )
