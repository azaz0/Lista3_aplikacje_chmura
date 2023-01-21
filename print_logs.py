import logging

default_log_format = "%(asctime)s - %(levelname)s - %(message)s"
level = input("Enter logging level (DEBUG, INFO): ").upper()


def set_logging(log_format):
    logging_level = getattr(logging, level, None)
    logging.basicConfig(level=logging_level, format=log_format)
    if level == "DEBUG":
        logging.debug("Logging is set to level: %s and format: %s", level, log_format)
    if level == "INFO":
        logging.info("Logging is set to level: %s and format: %s", level, log_format)


set_logging(default_log_format)
