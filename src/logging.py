"""
Sets up the logging globally for the application.
"""

import os
import logging

from dotenv import dotenv_values

config = dotenv_values(".env")


def setup_logging():
    LOGLEVEL = os.environ.get("LOGLEVEL", config["LOG_LEVEL"]).upper()
    logging.basicConfig(
        level=LOGLEVEL,
        filename=config["LOG_FILE"],
        filemode="a",
        format="%(asctime)s - %(levelname)s  %(message)s",
    )
