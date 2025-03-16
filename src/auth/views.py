from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.auth.models import TokenResponse, UserCreateRequest, UserRead
from src.auth.services import authenticate_user, create_user
from src.dependencies import AsyncSessionDep
from src.exceptions import HTTPExceptionResponseModel


auth_router = APIRouter(tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


@auth_router.post(
    "/auth/register",
    response_model=UserRead,
    status_code=201,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": HTTPExceptionResponseModel,
            "description": "Throws exception if user already exists",
        }
    },
)
async def register_user(db: AsyncSessionDep, data: UserCreateRequest):
    """
    Register a new user in the system.

    This endpoint allows users to create an account by providing their
    credentials

    **Response:**
    - `200 OK`: User registered successfully.
    - `400 Bad Request`: Username already exists or invalid input.
    """
    return await create_user(db, data=data)


@auth_router.post(
    "/auth/token",
    response_model=TokenResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": HTTPExceptionResponseModel},
        status.HTTP_404_NOT_FOUND: {"model": HTTPExceptionResponseModel},
    },
)
async def get_token(
    db: AsyncSessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user_obj = await authenticate_user(
        db=db, email=form_data.username, password=form_data.password
    )

    return {"token": user_obj.token, "user": user_obj}
