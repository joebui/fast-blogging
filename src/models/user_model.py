from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class User(Base):
    __tablename__ = "users"

    def __init__(self, name: str, hash: str):
        self.name = name
        self.password_hash = hash

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    password_hash: Mapped[str] = mapped_column()
