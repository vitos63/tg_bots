import logging
import sys

logger = logging.getLogger(__name__)


def devide_number(dividend: int | float, devider: int | float):
    logger.debug('log debug')
    logger.info('log info')
    logger.warning('log warning')
    logger.error('log error')
    logger.critical('log critical')
    try:
        return dividend/devider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')
