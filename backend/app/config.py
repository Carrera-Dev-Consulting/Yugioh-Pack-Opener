from enum import Enum
from functools import cache, cached_property
from pydantic_settings import BaseSettings
from pydantic.networks import MySQLDsn
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
    mysql_host: str = "localhost"
    mysql_port: int = 3306
    mysql_username: str = "root"
    mysql_password: str = "password"

    @cached_property
    def mysql_url(self):
        return MySQLDsn.build(
            scheme="mysql+pymysql",
            username=self.mysql_username,
            password=self.mysql_password,
            host=self.mysql_host,
            port=self.mysql_port,
            path="/yugioh_db",
        )


@cache
def server_config():
    return ServerConfig()
