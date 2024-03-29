from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):

    class Config():
        # orm_mode = True
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):

    # id: int
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        # orm_mode = True
        from_attributes = True


class ShowBlog(Blog):

    # id: int
    title: str
    body: str
    creator: ShowUser

    class Config():
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
