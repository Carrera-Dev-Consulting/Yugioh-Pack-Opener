from enum import Enum
from functools import cache
from pydantic_settings import BaseSettings
from secrets import token_hex


class LogFormat(str, Enum):
    JSON = "json"
    PRETTY = "pretty"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def __str__(self) -> str:
        return self.value


class ServerConfig(BaseSettings):
    env: str = "LOCAL"
    log_format: LogFormat = LogFormat.PRETTY
    log_level: LogLevel = LogLevel.DEBUG
    auth0_client_id: str
    auth0_client_secret: str
    auth0_domain: str = "gxldcptrick-yugioh-card-puller.us.auth0.com"
    app_secret_key: str = token_hex(28)

@cache
def server_config():
    return ServerConfig()
