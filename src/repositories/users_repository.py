from fastapi import Depends
from sqlalchemy.orm import Session
from configs.database import get_db_connection
from models.user_model import User


class UsersRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ):
        self.db = db

    def get_one(self, filters: dict) -> User | None:
        query = self.db.query(User)
        return query.filter_by(**filters).one_or_none()

    def create(self, name: str, hash: str) -> User:
        user = User(name=name, password_hash=hash)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
