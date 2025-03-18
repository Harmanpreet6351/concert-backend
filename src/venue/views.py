


from fastapi import APIRouter

from src.dependencies import AsyncSessionDep
from src.venue.models import VenueCreateRequest, VenueRead


venue_router = APIRouter(
    tags=["Venues"]
)


@venue_router.post(
    "/api/v1/venues",
    response_model=VenueRead
)
async def create_venue(
    db: AsyncSessionDep,
    data: VenueCreateRequest
):
    return await create_venue(db, data)