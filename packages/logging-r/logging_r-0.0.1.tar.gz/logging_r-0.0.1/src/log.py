import logging
import os
from logging.handlers import TimedRotatingFileHandler


def Logger(name: object = None, log_level: object = 'INFO') -> object:
    """
    custom function for logging
    :rtype: object
    :param name: log name
    :param log_level: log level for generating logs
    :return: None
    """

    level_dict = {'NOTSET': logging.NOTSET, 'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL}
    try:
        os.stat(os.path.abspath('logs'))
    except:
        os.mkdir(os.path.abspath("logs"))

    logger = logging.getLogger('Rotating Log')
    level_ = level_dict.get(log_level)
    print(level_)
    if level_ is not None:
        logger.setLevel(level_)
    else:
        logger.setLevel(logging.ERROR)

    fmt = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')

    if name is not None:
        path = os.path.join("logs", name + "_log.log")
    else:
        path = os.path.join("logs", "log.log")
    handler = TimedRotatingFileHandler(path,
                                       when='midnight',
                                       backupCount=5)
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logging.getLogger().addHandler(console)
    return logger
