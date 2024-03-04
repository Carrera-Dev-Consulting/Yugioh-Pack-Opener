import logging.config

from pythonjsonlogger.jsonlogger import JsonFormatter

from app.config import LogFormat, server_config


def configure_logging():
    config = server_config()
    if config.log_format == LogFormat.JSON:
        formatter = {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(name)s,%(processName)s,%(process)d,%(taskName)s,%(threadName)s,%(thread)d,%(asctime)s,%(filename)s,%(funcName)s,%(lineno)d,%(levelname)s,%(message)s",
        }
    else:
        formatter = {
            "format": f"[%(asctime)s][{config.env},%(levelname)s](%(name)s,%(processName)s,%(process)d,%(threadName)s,%(thread)d)(%(filename)s, %(funcName)s, %(lineno)d): %(message)s"
        }

    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"default": formatter},
        "handlers": {
            "stdout": {
                "formatter": "default",
                "level": config.log_level,
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "stderr": {
                "formatter": "default",
                "level": config.log_level,
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
        },
        "root": {"level": config.log_level, "handlers": ["stdout"]},
        "uvicorn.access": {"level": config.log_level, "handlers": ["stdout"]},
        "uvicorn.error": {"level": config.log_level, "handlers": ["stderr"]},
    }

    logging.config.dictConfig(log_config)

    return log_config
