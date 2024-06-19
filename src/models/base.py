from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc)
    )
