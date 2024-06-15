from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from fastapi import Depends
from configs.environment import get_env_var
from configs.logger import logger
from models.user_model import User
from repositories.users_repository import UsersRepository
from utils.constants import (
    JWT_ENCRYPTION_ALGO,
    UTF8_ENCODING,
)


class UsersService:
    def __init__(
        self, users_repo: UsersRepository = Depends()
    ):
        self.users_repo = users_repo
        self.jwt_secret = get_env_var("JWT_SECRET")

    def create(self, name: str, password: str) -> str:
        salt = bcrypt.gensalt()
        password_bytes = bytes(
            password,
            encoding=UTF8_ENCODING,
        )
        hashed = bcrypt.hashpw(password_bytes, salt)
        hashed = hashed.decode(UTF8_ENCODING)

        self.users_repo.create(name, hashed)
        return "success"

    def get_user_by_name(self, name: str) -> User | None:
        return self.users_repo.get_one({"name": name})

    def check_password(
        self, input_password: str, user: User
    ):
        input_password = bytes(
            input_password,
            encoding=UTF8_ENCODING,
        )
        password_hash = bytes(
            user.password_hash,
            encoding=UTF8_ENCODING,
        )

        is_valid = bcrypt.checkpw(
            input_password,
            password_hash,
        )
        return is_valid

    def generate_jwt(self, data: dict[str, str]) -> str:
        expired_date = datetime.now(
            timezone.utc
        ) + timedelta(days=90)
        headers = {
            "exp": expired_date.isoformat(),
            "iss": "fastapi",
        }

        encoded_jwt = jwt.encode(
            data,
            self.jwt_secret,
            algorithm=JWT_ENCRYPTION_ALGO,
            headers=headers,
        )
        return encoded_jwt

    def decode_jwt(
        self, token: str
    ) -> dict[str, str] | None:
        try:
            decoded = jwt.decode(
                token,
                self.jwt_secret,
                [JWT_ENCRYPTION_ALGO],
            )
            return decoded
        except Exception as e:
            logger.error("aaa", error=e)
            return None
