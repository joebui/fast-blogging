from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


@dataclass
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    password_hash: Mapped[str] = mapped_column()
