from fastapi import APIRouter

from src.auth.models import UserCreateRequest, UserRead
from src.auth.services import create_user
from src.dependencies import AsyncSessionDep


auth_router = APIRouter(tags=["Auth"])


@auth_router.post("/auth/register", response_model=UserRead)
async def register_user(db: AsyncSessionDep, data: UserCreateRequest):
    return await create_user(db, data=data)
