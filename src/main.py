from fastapi import FastAPI
from routers.auth_router import UsersRouter

app = FastAPI()

app.include_router(UsersRouter)


@app.get("/")
@app.get("/health")
def health_check() -> str:
    return "up"
