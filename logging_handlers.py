import logging

def logging_handler():
    # Create a custom logger
    logger = logging.getLogger('healthcare')
    logger.setLevel(logging.DEBUG)

    # Create a file handler for INFO level logs
    info_file_handler = logging.FileHandler('healthcare_info.log')
    info_file_handler.setLevel(logging.INFO)
    info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    info_file_handler.setFormatter(info_formatter)
    logger.addHandler(info_file_handler)

    # Create a stream handler for DEBUG level logs
    debug_stream_handler = logging.StreamHandler()
    debug_stream_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    debug_stream_handler.setFormatter(debug_formatter)
    logger.addHandler(debug_stream_handler)

    # Create a file handler for ERROR level logs
    error_file_handler = logging.FileHandler('healthcare_error.log')
    error_file_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    error_file_handler.setFormatter(error_formatter)
    logger.addHandler(error_file_handler)
