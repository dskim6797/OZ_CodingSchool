# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import engine, Base
from app.dependencies import get_db
from app.routers import user as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Day 1: 임시 테이블 생성 (Day 5에서 Alembic으로 대체)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(title="My Blog API (Day 2)", lifespan=lifespan)

app.include_router(user_router.router)


@app.get("/", summary="DB 연결 헬스 체크")
async def health(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    ok = result.scalar() == 1
    return {"db_connected": ok}
