import jwt

from app.models import Result


class CredentialService:
    def __init__(self, secret: str) -> None:
        self.secret = secret

    def sign_jwt(self, payload: dict) -> str:
        return jwt.encode(payload, key=self.secret.encode())

    def verify_jwt(self, payload: dict) -> Result[bool]:
        try:
            jwt.decode(payload, key=self.secret.encode())
        except jwt.exceptions.DecodeError:
            return Result(value=False, errors=["Failed to decode jwt"])
        return Result(value=True)
