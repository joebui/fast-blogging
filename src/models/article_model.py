from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


@dataclass
class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    owner_id: Mapped[int] = mapped_column()
    content: Mapped[str] = mapped_column()
