# app/db/session.py
from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "myuser"
    db_password: str = "mypass"
    db_name: str = "myblog"

    @property
    def async_db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

# postgresql에 적절하게 설정
engine = create_async_engine(
    settings.async_db_url,
    echo=True,
    pool_pre_ping=True,
    pool_size=10,        # 커넥션 풀 크기
    max_overflow=10,     # 커넥션 풀 최대 초과 크기
    pool_timeout=30,     # 커넥션 풀 타임아웃 시간 (30초)
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

Base = declarative_base()
