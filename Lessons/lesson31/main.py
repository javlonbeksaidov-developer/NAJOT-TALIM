from datetime import datetime

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from blog.db_config import engine, get_db
from blog.models import Article, Base
from blog.schemas import ArticleCreate

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/")
def welcome():
    return {"message": "Welcome to our Blog!"}


@app.post("/post-create/")
def create_new_post(article: ArticleCreate, db: Session = Depends(get_db)):  # noqa: B008
    try:
        new_article = Article(**article.model_dump())
        new_article.date_created = datetime.now()  # noqa: DTZ005
        db.add(new_article)
        db.commit()
        db.refresh(new_article)
        return {"message": "Created Article", "data": new_article}
    except Exception as error:  # noqa: BLE001
        return {"message": "Some error occurred!", "error": str(error)}



