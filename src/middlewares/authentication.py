from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from services.users_service import UsersService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    svc: UsersService = Depends(),
):
    current_user = svc.decode_jwt(token)
    if not current_user:
        raise HTTPException(
            status_code=403, detail="Access denied"
        )

    return current_user
