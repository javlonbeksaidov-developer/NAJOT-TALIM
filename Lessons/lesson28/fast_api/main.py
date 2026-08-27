from fastapi import FastAPI
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: int
    comment: str


class ApiResponceStandart(BaseModel):
    message: str
    error: str | None = None
    data: dict | list
    success: bool = True


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, FastApi!"}


@app.get("/admin")
def admin():
    return {"message": "Welcom Admin!"}


@app.get("/products/")
def products(category: str, start: int, stop: int):
    data = {"category": category, "start": start, "stop": stop}
    print(data)
    return data


@app.post("/product-create/")
def product_create(product: Product):
    print(product)
    return {"message": "created"}
