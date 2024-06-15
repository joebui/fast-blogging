UTF8_ENCODING = "utf-8"
JWT_ENCRYPTION_ALGO = "HS256"
NO_AUTH_PATHS = tuple(
    [
        # "/",
        # "/health",
        "/v1/users/login",
        "/v1/users/register",
        "/docs",
        "/openapi.json",
    ]
)
