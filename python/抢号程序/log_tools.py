import logging
logging.basicConfig(format='%(asctime)s %(funcName)s-%(lineno)d %(levelname)s:%(message)s', 
            level=logging.DEBUG,
            handlers=[logging.FileHandler("app.log"),logging.StreamHandler()]
            )
logger = logging.getLogger(__name__)

def log(msg):
    logger.info(msg)