import logging
import sys

# Root logger with default logging level
# print('---Root logger with default logging level--')
# logging.debug('I am debugging')  # will print a message to the console
# logging.info('I am collecting system info')
# logging.warning('low level issues')
# logging.error('throw errors')
# logging.critical('log critical messages')

# Basic Config Logging
print('---Basic Config Logging--')
log_format = '%(asctime)s %(filename)s: %(message)s'
date_format = '%d-%b-%Y %H:%M:%S'
filename = 'test.log'
print(logging.getLogger(__name__))
logging.basicConfig(level=logging.DEBUG, format=log_format, datefmt=date_format, filename=filename)
logging.info('This is a log message')

# Named logger with all level of logging
print('---Named logger with all level of logging--')
logger = logging.getLogger('logging_module')
print(logger.name)
logger.setLevel(logging.WARNING)

logger.debug('I am debugging')
logger.info('I am collecting system info')
logger.warning('low level issues')
logger.error('throw errors')
logger.critical('log critical messages')

# #Handlers 
print('---Handlers--')
logger = logging.getLogger('logging_module_handler')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('testfilehandler.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s  %(levelname)s: %(message)s',
                                               datefmt='%Y-%b-%d %H:%M:%S'))
file = open('teststreamfile.log', 'w')
stream_handler = logging.StreamHandler(file)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s  %(levelname)s: %(message)s',
                                               datefmt='%Y-%b-%d %H:%M:%S'))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info('test info level with handler')
logger.warning('test warning level with handler')
file.close()


vals = [1, 2]

try:
    print(vals[4])

except Exception as e:
    logger.error("exception occurred", exc_info=True)