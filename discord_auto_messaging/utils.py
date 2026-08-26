import logging

def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a logger instance with the specified name.

    Parameters:
    - name (str): The name of the logger.

    Returns:
    - logging.Logger: A configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to console handler
    ch.setFormatter(formatter)

    # Add console handler to logger
    if not logger.handlers:
        logger.addHandler(ch)

    return logger