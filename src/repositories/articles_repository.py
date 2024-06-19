from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from configs.database import get_db_connection
from models.article_model import Article


class ArticlesRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ):
        self.db = db

    def get_all(self) -> List[Article]:
        return self.db.query(Article).all()

    def get_one(self, filters: dict) -> Article | None:
        query = self.db.query(Article)
        return query.filter_by(**filters).one_or_none()

    def create(
        self,
        title: str,
        description: str,
        content: str,
        owner_id: int,
    ) -> Article:
        article = Article(
            title=title,
            description=description,
            content=content,
            owner_id=owner_id,
        )
        self.db.add(article)
        self.db.commit()
        self.db.refresh(article)
        return article
