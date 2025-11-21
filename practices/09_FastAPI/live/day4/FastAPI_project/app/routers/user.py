# app/routers/user.py
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db  # ✅ DI 일원화
from app.schemas.user import UserCreate, UserRead
from app.crud.user import (
    create_user,
    get_user_by_id,
    get_user_by_email,
    UserAlreadyExists,
    UserNotFound,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "",  # ✅ trailing slash 제거로 일관성 유지 (선호 스타일)
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    payload: UserCreate,
    response: Response,
    db: AsyncSession = Depends(get_db),
    ):
    try:
        user = await create_user(db, payload)
        # ✅ 201 Created 모범사례: Location 헤더 설정
        response.headers["Location"] = f"/users/{user.id}"
        return user
    except UserAlreadyExists as e:
        # ✅ 409로 매핑 + 표준화된 에러 바디
        raise HTTPException(status_code=e.status_code, detail=e.to_dict())


@router.get(
    "/{user_id}",
    response_model=UserRead,
)
async def read_user(
    user_id: Annotated[int, Path(ge=1)],  # ✅ 입력 검증
    db: AsyncSession = Depends(get_db),
    ):
    user = await get_user_by_id(db, user_id)
    if not user:
        err = UserNotFound(user_id=user_id)
        raise HTTPException(status_code=err.status_code, detail=err.to_dict())
    return user

@router.get(
    "/email/{user_email}",
    response_model=UserRead,
)
async def read_user_by_email(
    user_email: str,
    db: AsyncSession = Depends(get_db),
    ):
    user = await get_user_by_email(db, user_email)
    if not user:
        err = UserNotFound(user_email=user_email)
        raise HTTPException(status_code=err.status_code, detail=err.to_dict())
    return user