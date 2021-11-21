"""
File that contains the CustomLogger class.
"""

import logging


class CustomLogger:
    """
    Custom logger for the application.
    """

    def __init__(self, name, debug=False):
        """
        Initialize the logger
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
        # Save the log file as a .log file in the logs directory
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.FileHandler(
            f"logs/{name}.log", "a", encoding="utf-8"))

    def info(self, message):
        """
        log an info message
        """
        self.logger.info(message)

    def error(self, message):
        """
        log an error message
        """
        self.logger.error(message)

    def warning(self, message):
        """
        log a warning message
        """
        self.logger.warning(message)

    def debug(self, message):
        """
        log a debug message
        """
        self.logger.debug(message)

    def critical(self, message):
        """
        log a critical message
        """
        self.logger.critical(message)
