from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from custom_types.requests import RegisterRequestBody
from custom_types.responses import TokenResponse
from services.users_service import UsersService


UsersRouter = APIRouter()


@UsersRouter.post("/register")
async def register(
    user: RegisterRequestBody, svc: UsersService = Depends()
) -> str:
    return svc.create(user.name, user.password)


@UsersRouter.post("/auth")
async def authenticate(
    form_data: Annotated[
        OAuth2PasswordRequestForm, Depends()
    ],
    svc: UsersService = Depends(),
) -> TokenResponse:
    current_user = svc.get_user_by_name(form_data.username)
    if not current_user:
        raise HTTPException(
            status_code=404, detail="User not found"
        )

    is_valid = svc.check_password(
        form_data.password, current_user
    )
    if not is_valid:
        raise HTTPException(
            status_code=403,
            detail="Invalid username or password",
        )

    token = svc.generate_jwt(
        {"id": current_user.id, "name": current_user.name}
    )

    return {"acces_token": token, "token_type": "Bearer"}
