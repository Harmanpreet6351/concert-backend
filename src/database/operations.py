




from typing import Any, Literal, Type, TypedDict, TypeVar

from fastapi import HTTPException, status
from sqlalchemy import ColumnElement, select, asc, desc
from sqlalchemy.orm import InstrumentedAttribute, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import Base
from src.database.ext import paginate as paginate_query

ModelType = TypeVar("ModelType", bound=Base)

FilterSpecDef = list[
    tuple[
        str,
        Literal["eq", "neq", "gt", "lt", "gte", "lte"],
        Any
    ]
]

OrderSpecDef = list[
    tuple[
        str,
        Literal["asc", "desc"]
    ]
]

class PaginationArgs(TypedDict):
    page: int
    per_page: int

async def db_get_item_by_filter_spec(
    db: AsyncSession,
    model: Type[ModelType],
    *,
    filter_spec: FilterSpecDef = [],
    order_spec: OrderSpecDef = [],
    pagination_data: PaginationArgs | None = None,
    joined_loan_cols: list[InstrumentedAttribute] = [],
    raw_filters: list[ColumnElement] = [],
    many: bool = True
):
    stmt = select(model)

    for spec in filter_spec:
        if hasattr(model, spec[0]):
            if spec[1] == "eq":
                stmt = stmt.where(getattr(model, spec[0]) == spec[2])
            elif spec[1] == "neq":
                stmt = stmt.where(getattr(model, spec[0]) != spec[2])
            elif spec[1] == "gt":
                stmt = stmt.where(getattr(model, spec[0]) > spec[2])
            elif spec[1] == "lt":
                stmt = stmt.where(getattr(model, spec[0]) < spec[2])
            elif spec[1] == "gte":
                stmt = stmt.where(getattr(model, spec[0]) >= spec[2])
            elif spec[1] == "lte":
                stmt = stmt.where(getattr(model, spec[0]) <= spec[2])
    
    if len(joined_loan_cols) > 0:
        stmt = stmt.options(joinedload(*joined_loan_cols))

    if len(raw_filters) > 0:
        stmt = stmt.where(*raw_filters)

    for spec in order_spec:
        if hasattr(model, spec[0]):
            if spec[1] == "asc":
                stmt = stmt.order_by(asc(getattr(model, spec[0])))
            elif spec[1] == "desc":
                stmt = stmt.order_by(desc(getattr(model, spec[0])))

    if pagination_data is not None:
        return await paginate_query(db, stmt, page=pagination_data['page'], per_page=pagination_data["per_page"] or 10)
    

    result = await db.execute(stmt)

    if many == False:
        obj = result.scalar_one_or_none()

        if obj is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{obj.__class__} not Found"
            )
        
        return obj
    
    else:
        return result.scalars().all()



async def db_create_item(
    db: AsyncSession,
    model: Type[ModelType],
    data: dict
) -> ModelType:
    obj = model()
    for key, val in data.items():
        if hasattr(obj, key):
            setattr(obj, key, val)
    
    db.add(obj)
    await db.commit()

    await db.refresh(obj)

    return obj