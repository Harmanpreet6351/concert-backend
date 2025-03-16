from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User, UserCreateRequest


async def create_user(db: AsyncSession, *, data: UserCreateRequest) -> User:
    user_obj = User()
    user_obj.full_name = data.full_name
    user_obj.email = data.email

    user_obj.set_password(data.password)

    db.add(user_obj)

    await db.commit()
    await db.refresh(user_obj)

    return user_obj
