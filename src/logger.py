import logging
import os

from termcolor import colored


class CustomFormatter(logging.Formatter):
    _format = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: colored(_format, "white"),
        logging.INFO: colored(_format, "cyan"),
        logging.WARNING: colored(_format, "yellow"),
        logging.ERROR: colored(_format, "red"),
        logging.CRITICAL: colored(_format, "red", attrs=["bold"]),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


# logging.getLogger().setLevel(logging.INFO)
if os.getenv("PYTHON_LOG_DEBUG"):
    level = logging.DEBUG
else:
    level = logging.INFO

logging.getLogger().setLevel(level)
logHandler = logging.StreamHandler()
logHandler.setLevel(level)
logHandler.setFormatter(CustomFormatter())


logger = logging.getLogger("logger")
logger.propagate = False
logger.addHandler(logHandler)


class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("GET /healthcheck HTTP") == -1


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())
