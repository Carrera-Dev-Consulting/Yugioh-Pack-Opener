import logging.config

from pythonjsonlogger.jsonlogger import JsonFormatter

from app.config import LogFormat, server_config


def configure_logging():
    config = server_config()
    if config.log_format == LogFormat.JSON:
        formatter = {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(name)s,%(processName)s,%(process)d,%(taskName)s,%(threadName)s,%(thread)d,%(asctime)s,%(filename)s, %(funcName)s, %(lineno)d,%(levelname)-8s, %(message)s",
        }
    else:
        formatter = {
            "format": f"(%(name)s)%(processName)s%(process)d%(taskName)s%(threadName)s%(thread)d[%(asctime)s]([{config.env}]){{%(filename)s, %(funcName)s, %(lineno)d}}%(levelname)-8s - %(message)s"
        }

    log_config = {
        "formatters": {"default": formatter},
        "handlers": {
            "stdout": {
                "formatter": "default",
                "level": config.LOG_LEVEL,
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "stderr": {
                "formatter": "default",
                "level": config.LOG_LEVEL,
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
        },
    }

    logging.config.dictConfig(log_config)

    return log_config
