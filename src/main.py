from fastapi import FastAPI
from routers.articles_v1_router import ArticlesRouter
from routers.auth_router import UsersRouter

app = FastAPI()

app.include_router(UsersRouter)
app.include_router(ArticlesRouter)


@app.get("/")
@app.get("/health")
def health_check() -> str:
    return "up"
