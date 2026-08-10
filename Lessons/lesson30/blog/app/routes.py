from datetime import datetime

from app.database import load, save
from app.schemas import PostCreate, PostUpdate
from fastapi import APIRouter

router = APIRouter()

__table_name__ = "posts"


@router.get("/posts")
def get_post(start: int, skip: int):
    data = load()
    data = data[start - 1 : skip]
    return data


@router.get("/posts/{id}")
def get_post_id(id: int):
    data = load()
    for i, post in enumerate(data):
        if str(post["id"]) == str(id):
            post["views_count"] += 1
            data[i] = post
            save(data=data)
            return data


@router.get("/posts/like/{id}")
def like(id: int):
    data = load()
    for i, post in enumerate(data):
        if str(post["id"]) == str(id):
            post["likes_count"] += 1
            data[i] = post
            save(data=data)
            return data


@router.get("/posts/dislike/{id}")
def dislike(id: int):
    data = load()
    for i, post in enumerate(data):
        if str(post["id"]) == str(id):
            post["likes_count"] -= 1
            data[i] = post
            save(data=data)
            return data


@router.post("/posts")
def create_post(post: PostCreate):
    data = load()

    new_post = {
        "id": data[-1]["id"] + 1,
        "title": post.title,
        "description": post.description,
        "category": post.category,
        "views_count": 0,
        "likes_count": 0,
        "created_at": str(datetime.now()),  # noqa: DTZ005
    }
    data.append(new_post)
    save(data=data)

    return {"message": "Created"}


@router.put("/posts/{id}")
def update_post(id: int, post: PostUpdate):
    data = load()
    for i, updated_post in enumerate(data):
        if updated_post["id"] == id:
            updated_post["title"] = post.title
            updated_post["description"] = post.description
            updated_post["category"] = post.category

            data[i] = updated_post

        save(data=data)

    return {"message": "Updated"}


@router.delete("/posts/{id}")
def delete_post(id: int):
    data = load()
    for posts in data:
        if posts["id"] == id:
            data.remove(posts)

        save(data=data)

    return {"message": "Deleted"}
