import base64

from webauthn.helpers.structs import (
    PublicKeyCredentialRequestOptions,
    PublicKeyCredentialCreationOptions,
    PublicKeyCredentialDescriptor,
    PublicKeyCredentialType,
    UserVerificationRequirement,
    AuthenticatorSelectionCriteria,
    AuthenticatorAttachment,
    ResidentKeyRequirement,
    UserVerificationRequirement,
)
from webauthn.authentication.generate_authentication_options import (
    generate_authentication_options,
)

from webauthn.authentication.verify_authentication_response import (
    verify_authentication_response,
)
from webauthn.registration.verify_registration_response import (
    verify_registration_response,
)
from webauthn.registration.generate_registration_options import (
    generate_registration_options,
)

from webauthn.helpers.exceptions import InvalidAuthenticationResponse

from app.models import (
    User,
    LoginInfo,
    LoginRequest,
    PublicKeyRequest,
    RegistrationRequest,
)
from app.models.login import b64_decode
from app.repository.user_repository import authentication_keys, UserRepository
from .exceptions.login import InvalidLogin
from .credential_service import CredentialService


def remove_senstive_info(user: User):
    for key in authentication_keys:
        user.meta.pop(key)
    return user


def encode_base64(value: bytes) -> str:
    return str(base64.encodebytes(value))


RP_ID = "card-puller"
STATIC_HOST = "localhost:80"


class LoginService:
    def __init__(
        self, user_repo: UserRepository, credential_service: CredentialService
    ) -> None:
        self.user_repo = user_repo
        self.credential_service = credential_service

    def start_registration(
        self,
        request: PublicKeyRequest,
    ) -> PublicKeyCredentialCreationOptions:
        key = generate_registration_options(
            rp_id=RP_ID,
            rp_name="Yugioh Card Puller",
            user_id=request.user_id,
            user_name=request.user_id,
            user_display_name=request.user_id,
            attestation=request.attestation_type,
            authenticator_selection=AuthenticatorSelectionCriteria(
                authenticator_attachment=request.authenticator_type
                or AuthenticatorAttachment.CROSS_PLATFORM,
                resident_key=ResidentKeyRequirement.DISCOURAGED,
                user_verification=UserVerificationRequirement.REQUIRED,
            ),
        )
        return key

    def commit_user(self, request: RegistrationRequest) -> User:
        expected_challenge = request.challenge
        registration = verify_registration_response(
            credential=request.creds,
            expected_challenge=expected_challenge,
            expected_rp_id=RP_ID,
            expected_origin=STATIC_HOST,
        )
        user = User(
            username=request.user_id,
            email=request.email,
            meta={
                "public_key": encode_base64(registration.credential_public_key),
                "sign_count": registration.sign_count,
                "credential_id": encode_base64(registration.credential_id),
                "challenge": encode_base64(expected_challenge),
            },
        )
        out = self.user_repo.add_user(user)
        return remove_senstive_info(out)

    def login(self, request: LoginRequest) -> LoginInfo:
        user = self.user_repo.get_user_by_id(request.user_id)
        try:
            auth = verify_authentication_response(
                credential=request.creds,
                expected_challenge=request.challenge,
                expected_rp_id=RP_ID,
                expected_origin=STATIC_HOST,
                credential_public_key=b64_decode(user.meta["public_key"]),
                credential_current_sign_count=user.meta["sign_count"],
            )
            user.meta["sign_count"] = auth.new_sign_count
            return LoginInfo(
                user=remove_senstive_info(user),
                token=self.credential_service.sign_jwt({"id": user.username}),
            )
        except InvalidAuthenticationResponse:
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
