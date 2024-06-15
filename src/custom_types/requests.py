from typing import Annotated
from annotated_types import Len
from pydantic import BaseModel


class RegisterRequestBody(BaseModel):
    name: Annotated[str, Len(min_length=3, max_length=10)]
    password: Annotated[str, Len(min_length=3)]
