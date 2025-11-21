# app/schemas/user.py
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import StringConstraints


Username = Annotated[str, StringConstraints(min_length=3, max_length=50)]
Password = Annotated[str, StringConstraints(min_length=8, max_length=256)]


class UserBase(BaseModel):
    username: Username
    email: EmailStr


class UserCreate(UserBase):
    password: Password
    model_config = ConfigDict(extra="forbid")  # 선택


class UserRead(UserBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    model_config = ConfigDict(from_attributes=True)
