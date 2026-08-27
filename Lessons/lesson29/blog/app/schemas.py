from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    description: str
    category: str


class PostUpdate(BaseModel):
    title: str
    description: str
    category: str
