from webauthn.helpers.structs import (
    PublicKeyCredentialRequestOptions,
    PublicKeyCredentialDescriptor,
    PublicKeyCredentialType,
    UserVerificationRequirement,
)
from webauthn.authentication.generate_authentication_options import (
    generate_authentication_options,
)

from webauthn.authentication.verify_authentication_response import (
    verify_authentication_response,
)

from app.models import User, LoginInfo, LoginRequest, PublicKeyRequest, UserRequest
from app.repository.user_repository import authentication_keys, UserRepository
from .exceptions.login import InvalidLogin
from .credential_service import CredentialService


def remove_senstive_info(user: User):
    for key in authentication_keys:
        user.meta.pop(key)
    return user


RP_ID = "card-puller"
STATIC_HOST = "localhost:80"


class LoginService:
    def __init__(
        self, user_repo: UserRepository, credential_service: CredentialService
    ) -> None:
        self.user_repo = user_repo
        self.credential_service = credential_service

    def create_user(user: UserRequest):
        pass

    def login(self, request: LoginRequest) -> LoginInfo:
        user = self.user_repo.get_user_by_id(request.user_id)
        try:
            auth = verify_authentication_response(
                credential=request.creds,
                expected_challenge=request.challenge,
                expected_rp_id=RP_ID,
                expected_origin=STATIC_HOST,
                credential_public_key=user.meta["public_key"],
                credential_current_sign_count=user.meta["sign_count"],
            )
            user.meta["sign_count"] = auth.new_sign_count
            return self.credential_service.sign_jwt({"id": user.username})
        except:
            raise InvalidLogin()

    def get_public_key(
        self, request: PublicKeyRequest
    ) -> PublicKeyCredentialRequestOptions:
        user = self.user_repo.get_user_by_id(request.user_id)
        opts = generate_authentication_options(
            timeout=50_000,
            rp_id=RP_ID,
            allow_credentials=[
                PublicKeyCredentialDescriptor(
                    type=PublicKeyCredentialType.PUBLIC_KEY,
                    id=user.meta["credential_id"],
                )
            ],
            user_verification=UserVerificationRequirement.DISCOURAGED,
        )

        return opts
