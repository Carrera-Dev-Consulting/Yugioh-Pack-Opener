from logging import getLogger
from urllib.parse import urlencode
from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

from app.config import server_config

oauth = OAuth()
config = server_config()
logger = getLogger(__name__)

oauth.register(
    "auth0",
    client_id=config.auth0_client_id,
    client_secret=config.auth0_client_secret,
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=(
        f"https://{config.auth0_domain}/.well-known/openid-configuration"
    ),
)

router = APIRouter(tags=["oauth", "security"])


@router.get("/login", name="auth:login")
async def login(request: Request):
    callback_url = str(request.url_for("auth:callback"))
    logger.info(f"Creating callback url with: {callback_url}, {request.headers}")
    return await oauth.auth0.authorize_redirect(request, callback_url)


@router.get("/callback", name="auth:callback")
async def callback(request: Request):
    token = await oauth.auth0.authorize_access_token(request)

    user_info = token.get("userinfo")
    if user_info:
        request.session["user"] = user_info

    return RedirectResponse(request.url_for("user:info"))


@router.post("/logout")
async def logout(request: Request):
    request.session.clear()
    request_params = {
        "returnTo": "/",
        "client_id": config.auth0_client_id,
    }
    return RedirectResponse(
        f"https://{config.auth0_domain}/v2/logout?{urlencode(request_params)}"
    )


class Unauthenticated(ValueError):
    def __init__(self) -> None:
        super().__init__("Please Login to Continue")


def user(request: Request):
    if "user" not in request.session:
        raise Unauthenticated()
    return request.session["user"]


@router.get("/userinfo", name="user:info")
async def user_info(account=Depends(user)):
    return account
