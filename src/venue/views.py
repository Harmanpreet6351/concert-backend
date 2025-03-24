from fastapi import APIRouter

from src.database.operations import db_get_item_by_filter_spec
from src.dependencies import AsyncSessionDep, PaginationParamsDep
from src.venue.models import PaginatedVenueRead, Venue, VenueCreateRequest, VenueRead
from src.venue.service import create_venue as create_venue_db


venue_router = APIRouter(tags=["Venues"])


@venue_router.post("/venues", response_model=VenueRead)
async def create_venue(db: AsyncSessionDep, data: VenueCreateRequest):
    return await create_venue_db(db, data)


@venue_router.get("/venues", response_model=PaginatedVenueRead)
async def get_paginated_venues(
    db: AsyncSessionDep,
    page_data: PaginationParamsDep
):
    return await db_get_item_by_filter_spec(
        db,
        Venue,
        pagination_data={
            "page": page_data.page,
            "per_page": page_data.per_page
        }
    )
