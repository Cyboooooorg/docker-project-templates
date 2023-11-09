from __future__ import annotations

import os
import time

from loguru import logger


if __name__ == "__main__":
    try:
        logger.info(f"Starting the application {os.environ.get('APP_NAME')}...")
        
        while True:
            logger.debug("This is a debug message")
            time.sleep(1)
            logger.info("This is an info message")
            time.sleep(1)
            logger.warning("This is a warning message")
            time.sleep(1)
            logger.error("This is an error message")
            time.sleep(1)
            logger.critical("This is a critical message")

            time.sleep(5)
    except KeyboardInterrupt:
        logger.info(f"Stopping the application {os.environ.get('APP_NAME')}...")
