import logging
import sys

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

class logger(Object):
    def __init__(level):
        logging.basicConfig(level=LEVELS[level],
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%d-%m-%y %H:%M:%S',
                            filename='',
                            filemode='w')
        logger = logging.StreamHandler()
