from typing import List
from fastapi import Depends
from models.article_model import Article
from repositories.articles_repository import (
    ArticlesRepository,
)


class ArticlesV1Service:
    def __init__(
        self, articles_repo: ArticlesRepository = Depends()
    ):
        self.articles_repo = articles_repo

    def get_article(self, id: int) -> Article | None:
        return self.articles_repo.get_one({"id": id})

    def get_articles(self) -> List[Article]:
        return self.articles_repo.get_all()
