from fastapi import APIRouter
from src.auth.views import auth_router
from src.venue.views import venue_router
from src.concert.views import concert_router

api_router_v1 = APIRouter(prefix="/api/v1")


api_router_v1.include_router(auth_router)
api_router_v1.include_router(venue_router)
api_router_v1.include_router(concert_router)
