from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from blog.db_config import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=30), nullable=False)

    articles = relationship("Article", back_populates="category")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=100), nullable=False)
    body = Column(Text, nullable=False)
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)
    views = Column(Integer, default=0)
    date_created = Column(DateTime, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("Category", back_populates="articles")
    comments = relationship("Comments", back_populates="article")


class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(length=30), nullable=False)
    body = Column(Text, nullable=False)
    date_created = Column(DateTime, nullable=False)

    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)

    article = relationship("Article", back_populates="comments")
