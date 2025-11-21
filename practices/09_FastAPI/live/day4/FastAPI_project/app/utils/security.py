# app/utils/security.py
import os
from typing import Final

from passlib.context import CryptContext
from starlette.concurrency import run_in_threadpool


# ==========================
# Password hashing (Argon2)
# ==========================
# 튜닝값은 환경변수로 조정 가능(기본: 3회, 32MB, 병렬 1)
_PWD_CTX: Final = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
    argon2__time_cost=int(os.getenv("ARGON2_TIME_COST", "3")),
    argon2__memory_cost=int(os.getenv("ARGON2_MEMORY_COST", "32768")),  # KB
    argon2__parallelism=int(os.getenv("ARGON2_PARALLELISM", "1")),
    # 필요 시: argon2__hash_len=32, argon2__salt_size=16 등 추가 가능
)


def get_password_hash(plain: str) -> str:
    return _PWD_CTX.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    return _PWD_CTX.verify(plain, hashed)


# 운영 중 파라미터 상향 시 재해시 필요 여부 판단에 사용
def needs_rehash(hashed: str) -> bool:
    return _PWD_CTX.needs_update(hashed)


# async 버전 (이벤트 루프 차단 방지)
async def get_password_hash_async(plain: str) -> str:
    return await run_in_threadpool(_PWD_CTX.hash, plain)


async def verify_password_async(plain: str, hashed: str) -> bool:
    return await run_in_threadpool(_PWD_CTX.verify, plain, hashed)
