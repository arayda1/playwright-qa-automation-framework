import logging
import os


def get_logger():

    logger = logging.getLogger("PlaywrightFramework")

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


logger = get_logger()