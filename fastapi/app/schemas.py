from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class User(BaseModel):
    username: str
    password: str


class CreateUser(User):
    passwordcheck: str


class ShowUser(BaseModel):
    username: str

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None

