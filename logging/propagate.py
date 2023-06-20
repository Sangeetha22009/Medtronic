import logging

# Create the root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Create a child logger
child_logger = logging.getLogger('child')
child_logger.setLevel(logging.DEBUG)
child_logger.propagate = False  # Disable propagation


# Create a file handler for the root logger
root_handler = logging.FileHandler('root.log')
root_handler.setLevel(logging.INFO)
root_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Create a file handler for the child logger
child_handler = logging.FileHandler('child.log')
child_handler.setLevel(logging.DEBUG)
child_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Add the file handlers to the respective loggers
root_logger.addHandler(root_handler)
child_logger.addHandler(child_handler)

# Log messages using the child logger
child_logger.info('This is an info message from the child logger')
child_logger.warning('This is a warning message from the child logger')

# Log messages using the root logger
root_logger.info('This is an info message from the root logger')
root_logger.warning('This is a warning message from the root logger')
