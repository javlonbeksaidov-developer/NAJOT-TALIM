from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes import router

app = FastAPI()


app.include_router(router)

Base.metadata.create_all(engine)

@app.get("/")
def welcome():
    return {"message": "Welcome to my worker-salary project!"}
