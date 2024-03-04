from urllib.parse import urlencode
from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.config import server_config

oauth = OAuth()
config = server_config()
oauth.register(
    "auth0",
    client_id=config.auth0_client_id,
    client_secret=config.auth0_client_secret,
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=(
        f"https://{config.auth0_domain}/.well-known/openid-configuration"
    ),
)

router = APIRouter()


@router.get("/login")
async def login(request: Request):
    return await oauth.auth0.authorize_redirect(
        request, str(request.url_for("auth:callback"))
    )


@router.get("/callback")
async def callback(request: Request):
    token = await oauth.auth0.authorize_access_token(request)

    user_info = token.get("userinfo")
    if user_info:
        request.session["user"] = user_info["sub"]

    return RedirectResponse("/")


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
