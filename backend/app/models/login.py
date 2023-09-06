import base64

from pydantic import field_validator
from webauthn.helpers.structs import AuthenticationCredential

from .base import Base
from .user import User


def b64_decode(v: str):
    return base64.urlsafe_b64decode(v.encode())


class WebAuthenticationCredential(AuthenticationCredential):
    @field_validator("raw_id", mode="before")
    @classmethod
    def parse_raw_id(cls, v: str):
        return b64_decode(v)

    @field_validator("response", mode="before")
    @classmethod
    def parse_response(cls, v: dict):
        return {k: b64_decode(v) for k, v in v.items()}


class PublicKeyRequest(Base):
    user_id: str
    attestation_type: str
    authenticator_type: str


class UserRequest(Base):
    user_id: str
    creds: WebAuthenticationCredential


class LoginRequest(Base):
    user_id: str
    challenge: bytes
    creds: WebAuthenticationCredential

    @field_validator("challenge", mode="before")
    @classmethod
    def convert_to_bytes(cls, v: str):
        return b64_decode(v)


class LoginInfo(Base):
    user: User
    token: str
