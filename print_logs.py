import logging

default_log_format = "%(asctime)s - %(levelname)s - %(message)s"
level = input("Enter logging level [DEBUG, INFO, WARNING, CRITICAL, ERROR]: ").upper()


def set_logging(log_format):
    logging_level = getattr(logging, level, None)
    logging.basicConfig(level=logging_level, format=log_format)
    if level == "DEBUG":
        logging.debug('Protocol problem: %s', 'connection reset')
    if level == "INFO":
        logging.info('Protocol problem: %s', 'connection reset')
    if level == "WARNING":
        logging.warning('Protocol problem: %s', 'connection reset')
    if level == "ERROR":
        logging.error('Protocol problem: %s', 'connection reset')
    if level == "CRITICAL":
        logging.critical('Protocol problem: %s', 'connection reset')


set_logging(default_log_format)
