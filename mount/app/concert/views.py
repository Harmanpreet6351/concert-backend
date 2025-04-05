from fastapi import APIRouter

from app.concert.models import Concert, ConcertCreate, ConcertRead
from app.concert.services import add_concert_to_venue as add_concert_to_venue_db
from app.database.operations import db_create_item
from app.dependencies import AsyncSessionDep


concert_router = APIRouter(tags=["Concerts"])


@concert_router.post("/concerts", response_model=ConcertRead)
async def create_concert(data: ConcertCreate, db: AsyncSessionDep):
    return await db_create_item(db, Concert, data.model_dump(exclude_unset=True))


@concert_router.patch("/venue/{venue_id}/concerts/{concert_id}/add")
async def add_concert_to_venue(db: AsyncSessionDep, venue_id: int, concert_id: int):
    return await add_concert_to_venue_db(db, concert_id, venue_id)
