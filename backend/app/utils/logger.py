import logging

# Returns a configured logger instance for the given module name
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    handler.setFormatter(fmt)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
