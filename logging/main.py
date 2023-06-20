from fastapi import FastAPI
from logging_handlers import logging_handler
import logging

app = FastAPI()

logging_handler()  # Call the function to configure logging

@app.post('/healthcare/service')
def healthcare_service():
    logger = logging.getLogger('healthcare')
    logger.info('Executing healthcare service endpoint')
    logger.debug('Debugging information')

    # Execute algorithms and generate scoring
    # Add your code here

    try:
        # Simulating an error
        1 / 0
    except Exception as e:
        logger.error('An error occurred', exc_info=True)

    return {'score': 0.75}
