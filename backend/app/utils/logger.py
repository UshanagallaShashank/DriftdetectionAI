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


# Format error message with exception context for logging
def format_error(error: Exception, context: str = "") -> str:
    msg = f"{type(error).__name__}: {str(error)}"
    return f"{context} | {msg}" if context else msg
