from typing import Text

from pydantic import BaseModel


class ArticleCreate(BaseModel):
    title: str
    body: Text  # noqa: UP019
    category_id: int
