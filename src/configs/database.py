import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = os.getenv("DB_URL")

Engine = create_engine(DATABASE_URL, future=True, echo=True)
Session = sessionmaker(bind=Engine)


def get_db_connection():
    db = scoped_session(Session)
    try:
        yield db
    finally:
        db.close()
