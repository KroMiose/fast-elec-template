from loguru import logger

from .config import config


def init_logger():
    logger.add(
        f"{config.LOG_DIR}/app.log",
        rotation="10 MB",
        retention="10 days",
        level="INFO",
    )
