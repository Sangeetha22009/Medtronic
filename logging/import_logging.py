import logging_module
import logging.config
import yaml

print(logging_module.__name__)
print(logging_module.logger.name)

#logging custome data
logger_custome_data = logging.getLogger(logging_module.logger.name)
error_message = 'Authentication failed'
logger_custome_data.error(f'error: {error_message}')


#logging with fileconfig
logging.config.fileConfig(fname='log.conf')

logger = logging.getLogger('dev')
print(logger.name)
logger.debug('This is an debug message')
logger.info('This is an information message')

# with yaml config
with open('config.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())

logging.config.dictConfig(log_cfg)
logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)

logger.info('This is an info message')
logger.error('This is an error message')
