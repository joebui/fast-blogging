from typing import List
from fastapi import APIRouter, Depends, HTTPException
from custom_types.responses import ArticleResponse
from services.articles_v1_service import ArticlesV1Service


ArticlesRouter = APIRouter(prefix="/v1/articles")


@ArticlesRouter.get("/{id}")
async def get_article(
    id: int, svc: ArticlesV1Service = Depends()
) -> ArticleResponse:
    article = svc.get_article(id)
    if not article:
        raise HTTPException(
            status_code=404,
            detail="Article not found",
        )

    return article


@ArticlesRouter.get("")
async def get_articles(
    svc: ArticlesV1Service = Depends(),
) -> List[ArticleResponse]:
    return svc.get_articles()
